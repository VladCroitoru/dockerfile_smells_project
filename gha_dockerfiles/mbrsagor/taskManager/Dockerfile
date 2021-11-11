#base image
FROM python:3.8.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory
WORKDIR /app

##copy requirements
COPY requirements.txt /tmp/requirements.txt
#install requirements
RUN pip install -r /tmp/requirements.txt
#copy everythings
COPY . .
