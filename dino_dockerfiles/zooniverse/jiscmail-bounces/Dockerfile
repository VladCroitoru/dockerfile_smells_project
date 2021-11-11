FROM ubuntu:14.04

ADD requirements.txt /

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
    apt-get install -y python python-dev python-setuptools python-pip \
        python-lxml python-psycopg2 && \
    pip install -r requirements.txt

ADD process_bounces.py /

ENTRYPOINT [ "python", "/process_bounces.py" ]
