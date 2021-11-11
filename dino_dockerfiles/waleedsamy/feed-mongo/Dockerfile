FROM mongo:3.4

RUN apt-get update && \
    apt-get install -y vim curl python2.7 python-pip netcat-openbsd

RUN pip install awscli --upgrade

RUN mkdir -p /local /s3 /csv

ENV LOCAL_FILE ""

ENV S3_URI ""

ENV AWS_ACCESS_KEY_ID ""

ENV AWS_SECRET_ACCESS_KEY ""

ENV AWS_DEFAULT_REGION eu-central-1

ENV MONGO_HOST mongo

ENV MONGO_PORT 27017

ENV MONGO_DB local

ENV MONGO_COLLECTION hotels

ADD docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
