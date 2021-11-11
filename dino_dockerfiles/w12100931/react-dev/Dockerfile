#
# React JS Basic Development Environment
# Author: Jim Wu(Chung-Lin Wu)
# https://github.com/w12100931/react-dev
#

# Pull base image
FROM node:latest

MAINTAINER Chung-Lin Wu(w12100931@gmail.com)

# Install create-react-app and redux
RUN npm install -g create-react-app \
  && mkdir www \
  && cd www \
  && create-react-app my-app \
  && cd my-app \
  && npm install \
  && npm install redux --save \
  && npm install react-redux --save \
  && usermod -u 1001 www-data \
  && chown -Rf www-data.www-data /www \
  && chmod +x /www

# Prepare app directory
WORKDIR /www/my-app

# Mount a volume
VOLUME /www

EXPOSE 3000
CMD [ "npm", "start" ]
