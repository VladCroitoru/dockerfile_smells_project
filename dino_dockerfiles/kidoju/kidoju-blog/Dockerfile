# nodeJS official image
# built on debian 9 "stretch" (current stable release)
# see https://hub.docker.com/_/node/
# see also https://github.com/nodejs/docker-node/blob/master/10/Dockerfile
FROM node:10

# Maintained by Jacques L. Chereau
MAINTAINER jlchereau

# Set environment to production (and avoid installing devDependencies)
ENV NODE_ENV production

# Best practice documented at https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md#global-npm-dependencies
# ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

# Install prerequisites (especially to build mongoose)
# RUN apt-get update && apt-get install -y build-essential python
RUN apt-get update

# Copy our application
RUN mkdir -p /usr/src/
COPY . /usr/src/
WORKDIR /usr/src/

# Upgrade npm - required because anything between v5.2 and v5.5 does not work properly
# RUN npm install -g npm  - does not work: https://github.com/npm/npm/issues/15558
RUN yarn global add npm

# Add forever
# see https://github.com/foreverjs/forever
RUN npm install -g forever

# Install application modules
RUN npm install

# Delete cache (memba-blog and kidoju-blog)
# Do not comment as blog Dockerfile is copied from here
# and the if condition takes care of the specificity
RUN if [ -d /usr/src/webapp/cache ]; then rm -f /usr/src/webapp/cache/*; fi

# Expose nodeJS port
EXPOSE 3000

# Start node application
CMD [ "npm", "start" ]
