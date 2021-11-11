FROM python:2.7.11-slim

ADD . /srv
RUN pip install -r /srv/requirements.txt

EXPOSE 5000
ENV HOME /srv
WORKDIR /srv
