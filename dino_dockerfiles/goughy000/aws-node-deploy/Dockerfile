FROM node:6.9-slim

# Yarn Install
RUN \
  apt-get update && \
  apt-get install -y apt-transport-https && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install -y yarn && \
  apt-get clean

# Standard useful tools
RUN \
  apt-get update && \
  apt-get install -y jq zip build-essential && \
  apt-get clean

# Python
RUN \
  apt-get update && \
  apt-get install -y python2.7 python2.7-dev && \
  apt-get clean && \
  ln /usr/bin/python2.7 /usr/bin/python2 && \
  curl -O https://bootstrap.pypa.io/get-pip.py && \
  python2.7 get-pip.py && \
  rm get-pip.py

# AWS CLI Install
RUN \
  pip install awscli
