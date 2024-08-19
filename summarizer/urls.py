from .views import CustomAuthToken, GenerateBulletPointsView, GenerateSummaryView
from django.urls import path


urlpatterns = [
    path("token/", CustomAuthToken.as_view(), name="api_token_auth"),
    path("generate-summary/", GenerateSummaryView.as_view(), name="generate_summary"),
    path(
        "generate-bullet-points/",
        GenerateBulletPointsView.as_view(),
        name="generate_bullet_points",
    ),
]
