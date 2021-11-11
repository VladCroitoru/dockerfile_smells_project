FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-pip git python-dev yui-compressor

ENV PYTHONUNBUFFERED 1

RUN mkdir /code && mkdir /code/static
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 80
