FROM centos:7
MAINTAINER "patrick.douchement@fastconnect.fr"
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN yum install -y which
RUN yum install -y java-1.8.0-openjdk.x86_64
RUN yum install -y gcc
RUN yum install -y python-devel
RUN yum install -y unzip
RUN pip install virtualenv
