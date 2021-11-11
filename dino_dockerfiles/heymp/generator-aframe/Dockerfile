FROM node:6.11.4

# Sane defaults for setting up users
# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md#global-npm-dependencies
RUN npm install -g yo
RUN npm install -g generator-aframe@latest
USER node
WORKDIR /home/node/html
ENTRYPOINT [ "yo", "aframe" ]