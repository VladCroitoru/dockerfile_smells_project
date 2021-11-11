FROM python:3-slim

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=true

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--threads", "4", "--max-requests", "1000", "--worker-tmp-dir", "/tmp", "daemon:app"]
