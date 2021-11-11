FROM python:3
LABEL maintainer="Jacobmeide@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ./TheEye /TheEye
 