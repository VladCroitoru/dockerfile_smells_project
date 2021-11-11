FROM python:3

MAINTAINER Paula de la Hoz <inversealien@protonmail.com>

WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD gunicorn app:app --bind 0.0.0.0:80
