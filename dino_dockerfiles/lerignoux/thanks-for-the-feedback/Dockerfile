FROM python:3.9-alpine

MAINTAINER Erignoux Laurent <lerignoux@gmail.com>

RUN apk update && apk add zlib-dev jpeg-dev postgresql-libs && \
    apk add --virtual .build-deps build-base gcc musl-dev python3-dev libffi-dev openssl-dev postgresql-dev rust cargo

RUN mkdir /app
WORKDIR /app

ADD . /app/
RUN pip install --upgrade pip -r requirements.txt

RUN apk --purge del .build-deps

CMD ["python", "manage.py", "runserver", "0:8000"]
