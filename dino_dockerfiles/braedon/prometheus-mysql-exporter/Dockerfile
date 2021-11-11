FROM python:3.8-slim

WORKDIR /usr/src/app

COPY setup.py /usr/src/app/
COPY README.md /usr/src/app/
RUN pip install -e .

COPY prometheus_mysql_exporter/*.py /usr/src/app/prometheus_mysql_exporter/
COPY LICENSE /usr/src/app/

EXPOSE 9207

ENTRYPOINT ["python", "-u", "/usr/local/bin/prometheus-mysql-exporter"]
