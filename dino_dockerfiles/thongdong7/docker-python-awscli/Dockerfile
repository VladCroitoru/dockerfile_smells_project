FROM python:2.7-alpine3.7

RUN apk add --no-cache bash unzip gcc musl-dev libxml2-dev libxslt-dev && \
    pip install -U pip wheel && \
    pip install awscli boto3 requests pydash pyfunctional gevent redis backoff socket.io-emitter==0.1.5 python-redis-lock==3.2.0 filelock==3.0.4 kazoo==2.4.0 unicodecsv==0.14.1 beautifulsoup4==4.6.0 lxml==4.2.1 xlrd==1.0.0
