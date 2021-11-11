FROM python:2-alpine

MAINTAINER Jonjo McKay <jonjo@jonjomckay.com>

RUN apk add --no-cache build-base libffi libffi-dev openssl-dev \
  && pip install sftpsync \
  && apk del build-base libffi-dev openssl-dev
COPY sync.py /usr/local/

ENTRYPOINT ["/usr/local/sync.py"]
