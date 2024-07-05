FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --only frontend

COPY . /app

ENV PYTHONPATH="$PYTHONPATH:/app" 
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


ENTRYPOINT ["poetry", "run", "streamlit", "run", "frontend/tone_app.py", "--server.port=8501", "--server.address=0.0.0.0"]