FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV local

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

EXPOSE 8000