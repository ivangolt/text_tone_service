FROM python:3.11-slim

WORKDIR /code

ENV PYTHONPATH "${PYTHONPATH}:/code"
ENV PYTHONPATH=/code/src

COPY pyproject.toml poetry.lock /code/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir poetry==1.5.0 \
                              requests==2.32.3 \
                              uvicorn==0.30.0 \
                              transformers==4.41.2 \
                              fastapi==0.111.0 \
                              uvicorn==0.30.0 \
                              loguru==0.7.2 \
                              torch==2.3.0


RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi --no-root


COPY src /code
EXPOSE 8000

CMD ["uvicorn", "src.backend.app:app", "--host", "0.0.0.0", "--port", "8000"]

