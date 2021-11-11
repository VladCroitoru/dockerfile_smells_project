FROM node:13.7.0-alpine
LABEL maintainer="devops@rpsgroup.com"

COPY bin /opt/hfradar-dac-landing/bin
COPY public /opt/hfradar-dac-landing/public
COPY routes /opt/hfradar-dac-landing/routes
COPY views /opt/hfradar-dac-landing/views
COPY app.js package.json /opt/hfradar-dac-landing/

RUN apk update && \
    apk add yarn && \
    rm -rf /var/cache/apk/*

WORKDIR /opt/hfradar-dac-landing
RUN yarn

ENV NODE_ENV production

# don't run as root
USER node

CMD ["bin/www"]
