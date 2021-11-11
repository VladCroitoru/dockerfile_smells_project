FROM nikolaik/python-nodejs:python3.9-nodejs16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /noteadder

COPY Pipfile Pipfile.lock /noteadder/
RUN pip install pipenv && pipenv install --system


COPY . /noteadder/