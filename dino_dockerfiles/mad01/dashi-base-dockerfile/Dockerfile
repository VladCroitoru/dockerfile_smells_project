FROM debian:8
MAINTAINER Alexander Brandstedt

RUN apt-get update -y && \
    apt-get install -y \
        nodejs-legacy \
        gcc \
        npm \
        git \
        libyaml-dev \
        python-setuptools \
        python-pip \
        python-dev

RUN mkdir /opt/install
COPY . /opt/install
WORKDIR /opt/install

RUN npm install -g bower
RUN npm install -g react-tools
RUN bower install --allow-root
RUN pip install -r requirements.txt
