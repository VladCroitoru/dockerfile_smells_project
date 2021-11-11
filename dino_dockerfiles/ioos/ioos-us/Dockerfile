FROM node:13.7.0-alpine
LABEL maintainer="devops@rpsgroup.com"

COPY bin /opt/ioos-us/bin
COPY public /opt/ioos-us/public
COPY routes /opt/ioos-us/routes
COPY views /opt/ioos-us/views
COPY app.js assets.json gruntfile.js package.json /opt/ioos-us/

# install yarn, grunt; remove build cache
RUN apk update && \
    apk add yarn && \
    npm install -g grunt && \
    rm -rf /var/cache/apk/*

# change directory, install and grunt
WORKDIR /opt/ioos-us
RUN yarn && \
    /usr/local/lib/node_modules/grunt/bin/grunt

ENV NODE_ENV production

# don't run as root
USER node

CMD ["node", "bin/www"]
