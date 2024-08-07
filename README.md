# Model Service Api with Streamlit frontend

Example The ML service is a web application that provides an API for interacting with a machine learning model. It allows users to send queries with prediction data and get results back.

**Startup logic:**

When launched, the application initializes FastAPI, which handles HTTP requests. The app also connects to the machine learning model and loads it into memory for use in making predictions.

```
.
├── Docker
│   └── frontend
|        └── Dockerfile         # Docker image for frontend app
|   └── backend
|         └── Dockerfile        # Docker image for backend app
├── frontend
|      └── tone_app.py          # Streamlit app file for frontend part of app   
├── docker-compose.yml          # Docker container managing
├── pyproject.toml              # Dependencies
└── src
    ├── app.py                  # Main app, FastAPI initializing
    ├── api                     # Package with API routes
    │   ├── __init__.py
    │   └── routes              # Package with API routes
    │       ├── __init__.py
    │       ├── healthcheck.py  # Route to check the srvice status
    │       ├── predict.py      # Route for model predictions
    │       └── router.py       # Main router
    ├── schemas                 # Package with data models
    │   ├── __init__.py
    │   ├── healthcheck.py      # Model for service state responses
    │   └── requests.py         # Model for input requests to the API
    └── services                # Package with ML model
        ├── __init__.py
        ├── model.py            # ML model with prediction
        └── utils.py            # Supporting utilities
```

## Getting started with Docker Compose

`docker-compose up --build`

Web-server on

`http://localhost:8000`

UI on

`http://localhost:8000/docs`

App on 

`http://localhost:8501`


## Running local

`pip install --no-cache-dir poetry`

`poetry install --no-dev`

`poetry run uvicorn src.app:app --host localhost --port 8000`

and

`poetry run streamlit run frontend/tone_app.py`


# Example of work

![](docs/streamlit_service.png)