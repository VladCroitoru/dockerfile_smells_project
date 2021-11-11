FROM python:2.7.13-alpine

COPY app /opt/simple-web-prometheus

RUN pip install -r /opt/simple-web-prometheus/requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/opt/simple-web-prometheus/exporter.py"]