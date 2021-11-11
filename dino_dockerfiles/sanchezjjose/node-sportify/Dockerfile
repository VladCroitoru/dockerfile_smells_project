FROM node:4.0.0
MAINTAINER Jose Sanchez <sanchezjjose@gmail.com>


WORKDIR /usr/src/app


# http://www.clock.co.uk/blog/a-guide-on-how-to-cache-npm-install-with-docker
ADD package.json package.json


RUN npm install -g \
    nodemon \
    gulp-cli


RUN npm install


ADD . .


EXPOSE 3000


CMD ["npm", "start"]
