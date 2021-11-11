FROM python:2.7-alpine

RUN pip install elasticsearch-curator==5.4.1

COPY config.yml .
COPY actions.yml .

ENV LOG_LEVEL="INFO"
ENV DAYS_BEFORE_DELETE="7"
ENV ELASTICSEARCH_HOST=elasticsearch

ENTRYPOINT ["curator", "--config", "config.yml", "actions.yml"]
