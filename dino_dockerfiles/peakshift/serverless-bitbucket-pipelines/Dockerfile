FROM node:carbon
MAINTAINER Johns Beharry <johns@peakshift.com>

ENV DEBIAN_FRONTEND noninterative

RUN apt-get update \
  && apt-get install -y \
  apt-utils \
  sudo \
  build-essential \
  # PYTHON
  python \
  python-dev \
  # PIP
  python-pip \
  # AWS CLI
  && pip install awscli \
  # SERVERLESS CLI
  && npm install -g serverless \
  && sudo chown -R $USER:$(id -gn $USER) /root/.config
