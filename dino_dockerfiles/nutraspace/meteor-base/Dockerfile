# DOCKER-VERSION 18.03.1-ce-mac65
FROM  phusion/passenger-nodejs:0.9.32

RUN apt-get update

RUN apt-get install -y curl build-essential git software-properties-common g++ make openssl python2.7-dev python;

RUN curl http://nodejs.org/dist/v8.11.1/node-v8.11.1.tar.gz > node-v8.11.1.tar.gz; tar xvf node-v8.11.1.tar.gz; cd node-v8.11.1; ./configure; make; make install;

RUN npm config set registry http://registry.npmjs.org/
RUN npm install -g node-gyp;
 
RUN curl https://install.meteor.com/ | sh
