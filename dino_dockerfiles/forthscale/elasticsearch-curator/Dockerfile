FROM python:3.6.4-alpine3.7

RUN pip install -U --quiet elasticsearch-curator==5.5.4

ENTRYPOINT [ "/usr/local/bin/curator" ]
