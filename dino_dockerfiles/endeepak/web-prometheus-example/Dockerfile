FROM python:2.7.13-alpine

COPY app /opt/web-prometheus-example

RUN pip install -r /opt/web-prometheus-example/requirements.txt

EXPOSE 5000
EXPOSE 8000

ENTRYPOINT ["python", "/opt/web-prometheus-example/server.py"]