from python:3.5-alpine

RUN apk update  && \
    apk --no-cache --virtual add gcc openssh py-pip build-base libffi-dev openssh-client openssl-dev git && \
    apk add postgresql-dev



ADD ./requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt
RUN pip install psycopg2
