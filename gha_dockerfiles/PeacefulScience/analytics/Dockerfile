FROM ubuntu:latest

COPY requirements.txt /tmp/
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev git

RUN pip3 install --requirement /tmp/requirements.txt
