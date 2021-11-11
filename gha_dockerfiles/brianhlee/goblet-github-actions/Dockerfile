FROM python:3.9.5-alpine3.13

RUN pip install goblet-gcp

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
