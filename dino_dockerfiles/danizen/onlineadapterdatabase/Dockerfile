FROM ubuntu:16.04

RUN apt-get update && apt-get -y upgrade && apt-get -y install cron python python3
RUN apt-get install -y python3-pip build-essential python-virtualenv

COPY oadb /opt/oadb/oadb/
COPY data /opt/oadb/data/

ENV DJANGO_SETTINGS_MODULE oadb.settings.standalone
WORKDIR /opt/oadb/oadb
RUN ./buildoadb.sh -v venv

EXPOSE 8000

CMD ./runoadb.sh -v venv

