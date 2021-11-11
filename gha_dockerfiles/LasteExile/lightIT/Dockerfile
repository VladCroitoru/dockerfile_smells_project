FROM python:3.9

COPY . /app
WORKDIR /app

RUN apt update
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry config installer.parallel false
RUN poetry install
