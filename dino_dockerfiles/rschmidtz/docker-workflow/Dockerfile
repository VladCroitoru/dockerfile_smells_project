FROM ubuntu:16.04


# install dependencies
RUN apt-get -y update
RUN apt-get install -y python python-dev python-pip python-psycopg2
RUN apt-get install -y nginx supervisor


RUN mkdir /code

ADD app.py /code/app.py
# add requirements.txt and install
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

WORKDIR /code
