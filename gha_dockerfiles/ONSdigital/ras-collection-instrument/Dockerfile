FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential curl gunicorn gnupg
RUN pip install pipenv

WORKDIR /app

COPY . /app
RUN pipenv install --deploy --system
EXPOSE 8002
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "8", "--worker-class", "gevent", "--worker-connections", "1000", "--timeout", "30", "--keep-alive", "2", "app:app"]
