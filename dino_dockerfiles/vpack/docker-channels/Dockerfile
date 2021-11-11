FROM python:3.6.1
COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get -y install postgresql-client
RUN pip install -r requirements.txt
