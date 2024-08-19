# AI Text Summarizer

AI Text Summarizer is a Django-based API that generates summaries and bullet points from input text using Groq's language model. It provides endpoints for text summarization, bullet point generation, and user authentication.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- virtualenv

### Installation

1. Clone the repository:

```sh
git clone https://github.com/ardf/ai-text-summarizer.git
cd ai-text-summarizer
```

2. Create a virtual environment:

```sh
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```sh
  venv\Scripts\activate
```

- On macOS and Linux:

```sh
  source venv/bin/activate
```

4. Install the dependencies:

```sh
pip install -r requirements.txt
```

5. Set up environment variables:
   Create a `.env` file in the project root and add your Groq API key:

### Creating a Test User

To create a test user for API authentication:

1. Run the following command:

```sh
python manage.py createsuperuser
```

2. Follow the prompts to enter a username, email, and password for the test user.

### Running the Server

Start the development server:

```sh
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- `/api/token/`: Obtain an authentication token
- `/api/generate-summary/`: Generate a text summary
- `/api/generate-bullet-points/`: Generate bullet points from text
- `/swagger/`: API documentation (Swagger UI)

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST framework](https://www.django-rest-framework.org/) - For building the API
- [Groq](https://groq.com/) - Language model for text processing
