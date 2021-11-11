FROM python:3.5
ENV C_FORCE_ROOT 1

RUN adduser --disabled-password --gecos '' docker

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
