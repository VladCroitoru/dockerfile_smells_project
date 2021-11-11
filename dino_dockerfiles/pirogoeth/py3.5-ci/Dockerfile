FROM python:3.5-alpine
MAINTAINER Sean Johnson <pirogoeth@maio.me>

RUN apk update && \
    apk add bash     ## Install bash for CI scripts.

RUN apk add py-virtualenv python-dev gcc openssl libc-dev
