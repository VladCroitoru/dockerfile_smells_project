FROM python:3.10-alpine

RUN apk add build-base openssl-dev libffi-dev

RUN pip3 install pipenv

WORKDIR /pjatk

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install

RUN apk del build-base openssl-dev libffi-dev

COPY common/ /pjatk/common/

COPY discordcat/ /pjatk/discordcat/

COPY webgate/ /pjatk/webgate/

COPY templates/ /pjatk/templates/

ENV PYTHONPATH "${PYTHONPATH}:/pjatk/"

ENV TZ "Europe/Warsaw"
