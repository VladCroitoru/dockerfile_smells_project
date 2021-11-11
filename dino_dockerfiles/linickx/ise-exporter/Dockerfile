FROM python:alpine
MAINTAINER  Nick <linickx.com>
RUN pip install Flask pyyaml requests

COPY ise-exporter.py  /bin/ise-exporter
COPY ise.yml       /etc/ise-exporter/ise.yml

EXPOSE      9123
ENTRYPOINT  [ "/bin/ise-exporter" ]
