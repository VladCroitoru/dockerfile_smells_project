FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
# set work directory
WORKDIR /usr/src/app
# set environment variables
# install dependencies
RUN apt-get update && apt-get install -y git
RUN pip install -U pip

COPY requirements.txt ./
RUN pip install -r requirements.txt