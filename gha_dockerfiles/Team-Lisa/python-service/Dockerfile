FROM python:3.9-slim

RUN pip install poetry

RUN mkdir /app
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
CMD mkdir covid_service
COPY ./api /app/api

CMD uvicorn api.main:app --host 0.0.0.0 --port $PORT
