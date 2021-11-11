# Pull base image

FROM python:3.9-slim

# Update base
RUN apt-get update
RUN apt-get install -y --reinstall build-essential

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /code

# Install dependencies

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/