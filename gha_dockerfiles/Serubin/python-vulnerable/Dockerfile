FROM alpine:3.12

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache \
    python3 \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    build-base \
    libressl-dev \
    openssl-dev \
    musl-dev \
    libffi-dev \
    && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY ./ /opt/

RUN cd /opt/ && pip3 install --no-cache -r requirements.txt

RUN apk del \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    build-base \
    libressl-dev \
    musl-dev \
    libffi-dev \
