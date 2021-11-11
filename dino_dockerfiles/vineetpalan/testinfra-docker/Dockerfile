FROM python:2.7.14-alpine 

RUN apk --update \
    add --no-cache gcc \
    musl-dev \
    python-dev \
    libffi \
    libffi-dev \
    unixodbc-dev \
    openssl-dev \
    build-base \
    py-pip \
&&  pip install cffi==1.10 \
&&  pip install requests \
&&  pip install paramiko \
&&  pip install testinfra


CMD ["/bin/sh"]
