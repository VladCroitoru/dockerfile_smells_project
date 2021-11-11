FROM python:2.7-alpine

RUN apk add --update \
  ca-certificates \
  && pip install boto3 \
  && rm -rf /var/cache/apk/*
COPY lookup.py /lookup.py
ENTRYPOINT ["/lookup.py"]
