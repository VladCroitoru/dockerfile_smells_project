FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN locale-gen en_US en_US.UTF-8
ENV LANG en_US.UTF-8

#To build AMC
RUN apt-get install -y build-essential python-dev python-pip man libffi-dev wget
RUN sudo pip install markupsafe paramiko ecdsa pycrypto bcrypt

ENV AMC_VERSION 3.6.6
#AMC
RUN wget -O amc.deb http://www.aerospike.com/download/amc/${AMC_VERSION}/artifact/ubuntu12 && \
    dpkg -i amc.deb && \
    rm amc.deb

CMD ["/opt/amc/bin/gunicorn", "--config=/etc/amc/config/gunicorn_config.py", "flaskapp:app"]
