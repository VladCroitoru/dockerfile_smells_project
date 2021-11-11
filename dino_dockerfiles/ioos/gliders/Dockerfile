FROM node:13.7.0-alpine
LABEL maintainer="devops@rpsgroup.com"

COPY bin /opt/gliders/bin
COPY public /opt/gliders/public
COPY routes /opt/gliders/routes
COPY views /opt/gliders/views
COPY app.js package.json /opt/gliders/

# install
WORKDIR /opt/gliders
RUN yarn

# don't run as root
USER node

ENV NODE_ENV production

CMD ["node", "bin/www"]
