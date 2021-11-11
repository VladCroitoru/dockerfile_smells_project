FROM python:2.7.8-slim

RUN pip install --quiet elasticsearch-curator

COPY curator.yml .
COPY actions.yml .

ENTRYPOINT [ "/usr/local/bin/curator", "--config", "curator.yml", "actions.yml"]