FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends vim && \
    apt-get install -y --no-install-recommends netcat 

COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

RUN apt-get autoremove -y --purge && \
    apt-get clean -y 

COPY ./django/blog/entrypoint.sh /app/entrypoint.sh

