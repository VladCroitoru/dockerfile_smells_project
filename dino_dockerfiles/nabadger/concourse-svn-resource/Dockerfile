FROM node:5
MAINTAINER "William Matthews" robophred@gmail.com

WORKDIR /opt/resource
COPY check.js check
COPY in.js in
COPY out.js out

COPY shared.js shared.js
COPY package.json package.json

RUN apt-get update --yes && \
    apt-get install --yes \
    	    subversion \
	    locales locales-all && \
    apt-get autoremove --yes && \
    apt-get clean --yes && \
    npm install --quiet

RUN chmod a+x check in out

