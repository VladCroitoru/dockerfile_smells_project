FROM python:3.8-slim-buster as base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install python-dotenv

COPY . .

CMD gunicorn -b 0.0.0.0:$PORT scrumhub.main:app

 FROM base as test

 CMD python -m unittest tests.database.ProjectTest
