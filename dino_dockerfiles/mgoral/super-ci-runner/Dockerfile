FROM ubuntu:latest

RUN apt-get -y update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get -y update && apt-get install -y \
    git \
    zip \
    virtualenv \
    python3.3 \
    libpython3.3-dev \
    python3.4 \
    libpython3.4-dev \
    python3.5 \
    libpython3.5-dev \
    python3.6 \
    libpython3.6-dev \
    python3.7 \
    libpython3.7-dev \
    python-pip \
    python3-pip
