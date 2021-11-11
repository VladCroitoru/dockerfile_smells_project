FROM python:3.8-slim AS base

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]