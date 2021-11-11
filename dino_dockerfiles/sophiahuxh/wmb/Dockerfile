# VERSION 1.0
# DOCKER-VERSION 1.12.1
# To build:
# 1. Install docker (http://docker.io)
# 2. Checkout source: git@github.com:gasi/docker-node-hello.git
# 3. Build container: docker build .

FROM    node:4

# App
ADD . /src
# Install app dependencies
RUN cd /src; npm install

WORKDIR /src

EXPOSE  80
CMD ["node", "keystone.js"]
