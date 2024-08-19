# Create your views here.
import os

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

from .serializers import TextSummarySerializer

from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model="mixtral-8x7b-32768")


class CustomAuthToken(ObtainAuthToken):
    """
    Custom authentication token view.

    This class handles user authentication and returns a token along with user details.
    It extends the ObtainAuthToken class to provide additional user information in the response.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for authentication.

        This method validates user credentials, creates or retrieves an authentication token,
        and returns the token along with user ID and email.

        Returns:
            Response: A response containing the authentication token, user ID, and email.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class GenerateSummaryView(APIView):
    """
    View for generating text summaries.

    This class provides an endpoint to create summaries from input text.
    It requires authentication and uses a language model to generate the summary.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TextSummarySerializer

    @swagger_auto_schema(
        request_body=TextSummarySerializer, responses={201: TextSummarySerializer}
    )
    def post(self, request):
        """
        Handle POST requests to generate a summary.

        This method takes input text, generates a summary using a language model,
        saves the result, and returns the created TextSummary instance.

        Returns:
            Response: A response containing the created TextSummary data with HTTP 201 status.
        """
        text = request.data.get("text")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        summary_template = """
        Please provide a concise summary of the following text:
        
        {text}
        
        Summary:
        """
        summary_prompt = PromptTemplate(
            template=summary_template, input_variables=["text"]
        )

        chain = summary_prompt | llm
        response = chain.invoke(text)
        summary = response.content
        summary_instance = serializer.save(summary=summary)
        return Response(data=self.serializer_class(summary_instance).data, status=201)


class GenerateBulletPointsView(APIView):
    """
    View for generating bullet points from text.

    This class provides an endpoint to create bullet points summarizing key points from input text.
    It requires authentication and uses a language model to generate the bullet points.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TextSummarySerializer

    @swagger_auto_schema(
        request_body=TextSummarySerializer, responses={201: TextSummarySerializer}
    )
    def post(self, request):
        """
        Handle POST requests to generate bullet points.

        This method takes input text, generates bullet points using a language model,
        saves the result, and returns the created TextSummary instance.

        Returns:
            Response: A response containing the created TextSummary data with HTTP 201 status.
        """
        text = request.data.get("text")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        bullet_points_template = """
        Please generate a list of bullet points summarizing the key points from the following text:
        
        {text}
        
        Bullet points:
        """
        bullet_points_prompt = PromptTemplate(
            template=bullet_points_template, input_variables=["text"]
        )
        chain = bullet_points_prompt | llm
        response = chain.invoke(text)
        bullet_points = response.content
        bullet_points_instance = serializer.save(bullet_points=bullet_points)
        return Response(
            data=self.serializer_class(bullet_points_instance).data, status=201
        )
