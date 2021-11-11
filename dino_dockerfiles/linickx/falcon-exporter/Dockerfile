FROM python:alpine
MAINTAINER  Nick <linickx.com>
RUN pip install Flask pyyaml requests

COPY falcon-exporter.py  /bin/falcon-exporter
COPY ca.pem  /etc/falcon-exporter/ca.pem

EXPOSE      9122
ENTRYPOINT  [ "/bin/falcon-exporter" ]
