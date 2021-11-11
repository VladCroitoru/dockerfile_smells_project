FROM ubuntu:xenial

COPY . /src

WORKDIR /src

RUN apt-get update -y
RUN apt-get install -y --assume-yes --no-install-recommends apt-utils 
RUN apt-get install -y python3 python3-pip
RUN pip3 install Werkzeug Jinja2 Flask
RUN pip3 install prometheus_client
