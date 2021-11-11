FROM python:3.9-slim
ENV PYTHONNUNBUFFERED 1
WORKDIR /code
RUN apt-get update \
    && apt-get install -y gettext \
    && apt-get install -y gcc \
    && apt-get install -y libpq-dev
COPY requirements.txt /code
RUN pip install --default-timeout=100 -r requirements.txt