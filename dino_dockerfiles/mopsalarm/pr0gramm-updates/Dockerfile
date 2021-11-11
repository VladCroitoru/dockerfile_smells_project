FROM python:3.7.4-slim-buster
MAINTAINER Mopsalarm

EXPOSE 8080

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["python3", "-u", "-m", "bottle", "-s", "waitress", "-b", "0.0.0.0:8080", "main"]
