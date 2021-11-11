FROM alpine:latest
MAINTAINER stive.hu@gmail.com
RUN apk add --update  --no-cache \
    python \
    python-dev \
    py-pip \
    curl \
    autoconf \
    gcc \
    g++ \
    make \
    libffi-dev \
    postgresql-dev

RUN curl -O https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.1/pip/pgadmin4-2.1-py2.py3-none-any.whl --no-verbose
RUN pip install --upgrade pip
RUN yes | pip install pgadmin4-2.1-py2.py3-none-any.whl
RUN sed -i "s/SERVER_MODE = True/SERVER_MODE = False/" /usr/lib/python2.7/site-packages/pgadmin4/config.py
RUN sed -i "s/DEFAULT_SERVER = '127.0.0.1'/DEFAULT_SERVER = '0.0.0.0'/" /usr/lib/python2.7/site-packages/pgadmin4/config.py

RUN apk del curl \
    autoconf \
    gcc \
    g++ \
    make \
    libffi-dev \
    openssl-dev 
RUN rm -rf /var/cache/apk/*
VOLUME /root
WORKDIR /usr/lib/python2.7/site-packages/pgadmin4
EXPOSE 5050
ENTRYPOINT ["python", "/usr/lib/python2.7/site-packages/pgadmin4/pgAdmin4.py"]