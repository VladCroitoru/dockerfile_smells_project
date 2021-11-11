FROM python:3.8.3-alpine

ARG dev_req="-r /tmp/requirements-dev.txt"

RUN apk add --update \
    make \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements-dev.txt /tmp/requirements-dev.txt
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    && pip install -r /tmp/requirements.txt ${dev_req} \
    && apk del .build-deps && rm -rf /var/cache/apk/*

COPY . /src

WORKDIR /src

CMD ["python","app.py"]
