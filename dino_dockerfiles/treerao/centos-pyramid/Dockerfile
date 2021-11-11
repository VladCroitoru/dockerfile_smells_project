FROM     centos:latest
MAINTAINER Ramana Rao <treerao@gmail.com>

# load base packages w/ yum
RUN yum install -y git gcc libffi-devel openssl-devel python-devel postgresql-devel libxml2-devel libxslt-devel
COPY ./requirements.txt .

RUN curl https://bootstrap.pypa.io/get-pip.py >get-pip.py && \
    python get-pip.py && \
    rm get-pip.py &&\
    pip install -r requirements.txt

EXPOSE 6543

