# Docker file for tsb
# Use an official Python runtime as a parent image
FROM python:3.8-buster
MAINTAINER Roald Storm <roald.storm@niva.no>

RUN apt-get update &&  apt-get install -y --no-install-recommends libgeos-dev

# Set the working directory to /app
WORKDIR /app
RUN pip install psycopg2
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
RUN black --check .
RUN pycodestyle --config .pycodestyle src
RUN mypy src
RUN pip install .
RUN pytest

ARG GIT_COMMIT_ID=unknown
LABEL git_commit_id=$GIT_COMMIT_ID
ENV GIT_COMMIT_ID=$GIT_COMMIT_ID

# Start gunicorn
CMD ["python", "/app/src/odm2_postgres_api/main.py"]
