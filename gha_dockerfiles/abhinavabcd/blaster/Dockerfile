FROM python:3.6-alpine

COPY pip_requirements.txt /

RUN apk add --no-cache \
    libev \
    python3-dev build-base \
&& pip install -r pip_requirements.txt \
&& apk del python3-dev build-base

COPY blaster/ /usr/local/lib/python3.6/site-packages/blaster/

