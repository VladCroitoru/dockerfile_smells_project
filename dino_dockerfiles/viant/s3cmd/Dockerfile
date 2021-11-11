FROM ubuntu:latest

RUN apt-get update &&\
    apt-get install -y wget unzip &&\
    apt-get install -y python2.7 python-setuptools

RUN wget https://github.com/s3tools/s3cmd/archive/master.zip &&\
    unzip master.zip &&\
    cd s3cmd-master &&\
    python setup.py install
