# Base image with initial set of node modules installed into /src/node_modules
FROM gpmikep/docker-node-chrome

RUN mkdir -p /src
WORKDIR /src

# currently disabled due to problems with npm update in docker under aufs
# https://github.com/npm/npm/issues/9863#issuecomment-197328092

#ADD package.json .
#RUN npm install
