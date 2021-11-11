FROM ubuntu:latest
RUN apt-get update -yqq
RUN apt-get install curl -y
RUN curl -sSL https://get.docker.com/ | sh
RUN apt-get install python-pip -yqq
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install awscli
