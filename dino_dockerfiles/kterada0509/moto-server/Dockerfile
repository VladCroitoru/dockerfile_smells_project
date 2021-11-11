FROM python:2.7-wheezy

MAINTAINER Kentaro Terada kterada.0509sg@gmail.com

RUN pip install moto \
    && pip install flask

COPY endpoints.json /opt/moto/

# Default port that moto listens on.
EXPOSE 5000


CMD ["moto_server","--help"]