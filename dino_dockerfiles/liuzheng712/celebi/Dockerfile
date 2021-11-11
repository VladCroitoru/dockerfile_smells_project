FROM ubuntu
MAINTAINER liuzheng "liuzheng712@gmail.com"

RUN apt-get update && \
    apt-get install -qqy python python-setuptools python-dev && \
    easy_install pip

RUN pip install ansible django

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root
