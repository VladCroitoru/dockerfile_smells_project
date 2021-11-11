FROM node:latest
MAINTAINER haha1903

# 80 = HTTP, 443 = HTTPS, 3000 = MEAN.JS server, 35729 = livereload
EXPOSE 80 443 3000 35729

RUN npm install -g gulp-cli gulp bower

RUN mkdir -p /opt/mean.js/public/lib
WORKDIR /opt/mean.js

# Install npm packages
COPY package.json /opt/mean.js/package.json
COPY package-lock.json /opt/mean.js/package-lock.json
RUN NODE_ENV=development npm install

# Install bower packages
COPY bower.json /opt/mean.js/bower.json
COPY .bowerrc /opt/mean.js/.bowerrc
RUN bower install --allow-root --config.interactive=false

