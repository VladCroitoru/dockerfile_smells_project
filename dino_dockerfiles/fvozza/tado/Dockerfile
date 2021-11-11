FROM node:4-onbuild
MAINTAINER Francesco Vozza <fvozza at gmail dot com>

# Install dependencies
# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
# The idea here is that if the package.json file changes (line 14) then 
# Docker will re-run the npm install sequence (line 15)… otherwise Docker 
# will use our cache and skip that part.

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

# From here we load our application's code in, therefore the previous docker
# "layer" thats been cached will be used if possible

WORKDIR /opt/app
ADD . /opt/app

CMD ["node", "tado.js"]