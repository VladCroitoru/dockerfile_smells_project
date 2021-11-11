FROM python:3.6-slim

EXPOSE 8080

COPY requirements.txt opsgenie-proxy.py ./

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "opsgenie-proxy:app", "--workers", "1", "--preload"]
