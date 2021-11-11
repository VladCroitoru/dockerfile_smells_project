# syntax=docker/dockerfile:1

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
