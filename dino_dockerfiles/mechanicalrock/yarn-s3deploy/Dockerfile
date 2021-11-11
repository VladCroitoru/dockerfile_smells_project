FROM beevelop/nodejs-python:latest
MAINTAINER William Sia <williamsia82@gmail.com>

# Prerequisite for PhantomJS.
RUN \
  apt-get update && \
  apt-get -y install libfontconfig && \
  rm -rf /var/lib/apt/lists/*

RUN \
  npm install -g yarn && \
  npm install -g phantomjs-prebuilt && \
  npm install -g s3-deploy