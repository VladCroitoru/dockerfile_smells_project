FROM ubuntu:focal

RUN apt-get update -y && \
    apt-get install software-properties-common -y

# Install REDIS
RUN add-apt-repository ppa:redislabs/redis -y && \
    apt-get update -y && \
    apt-get install redis -y

# Install Python3
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update -y && \
    apt install python3.8 python3-pip -y

# Install quantum-robot
COPY ./ /quantum-robot
WORKDIR /quantum-robot
RUN set -ex && pip install -e /quantum-robot

# Test the package
RUN service redis-server start && pytest .

EXPOSE 8899