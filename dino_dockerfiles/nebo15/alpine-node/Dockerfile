FROM node:6.9-alpine

MAINTAINER Nebo#15 support@nebo15.com

ENV REFRESHED_AT=2017-02-19 \
    NODE_VERSION=6.9.5 \
    TERM=xterm \
    HOME=/app

# Create app dir
RUN mkdir ${HOME} && \
    chown -R node:node ${HOME}

# Update NPM and install PM2
RUN npm install -g pm2 && \
    npm cache clean

# Cleanup container
RUN rm -rf \
    /usr/share/man \
    /tmp/* /var/cache/apk/* \
    /root/.npm \
    /root/.node-gyp \
    /root/.gnupg \
    /usr/lib/node_modules/npm/man \
    /usr/lib/node_modules/npm/doc \
    /usr/lib/node_modules/npm/html \
    /usr/lib/node_modules/npm/scripts

WORKDIR ${HOME}

# Start apps under PM2 supervision
# TODO: Replace with http://pm2.keymetrics.io/docs/usage/docker-pm2-nodejs/
CMD ["pm2 start --log-type json --merge-logs --no-daemon static/server.server.js"]
