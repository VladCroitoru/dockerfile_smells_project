#
# Build
# docker build -t chamerling/dockerhub2slack .
#
# Run
# docker run -d -p 3000:3000 -e "SLACK_WEBHOOK=http://YOUR_INCOMING_WEBHOOK" chamerling/dockerhub2slack

FROM node:0.10.36-slim
MAINTAINER Christophe Hamerling <chamerling@linagora.com>

COPY package.json /var/www/package.json
RUN cd /var/www && npm install --production

WORKDIR /var/www
CMD ['node', 'dist/server/index.js']
