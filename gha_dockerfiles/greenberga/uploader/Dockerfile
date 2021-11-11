FROM python:3.6

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install -d

ENTRYPOINT /bin/bash
