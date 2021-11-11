# Build frontend
FROM node:16-alpine3.11 AS frontend
RUN mkdir /app
WORKDIR /app
ADD ./frontend/ /app/
RUN npm install --production
RUN npm run build

# Build backend
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 AS backend
WORKDIR /app
RUN pip install poetry
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client

COPY ./backend/ /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

RUN rm -rf /app/static/*
COPY --from=frontend /app/public/static/ /app/static/
COPY --from=frontend /app/public/index.html /app/templates/

ENV APP_MODULE="main:app"
