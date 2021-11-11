FROM node:5.5

RUN npm install -g jshint@~2.9.1
RUN npm install -g bower@~1.7.2
RUN npm install -g nodemon@~1.8.1
RUN npm install -g gulp-cli@~1.2.0

VOLUME /usr/src/app
WORKDIR /usr/src/app

COPY .npmrc /root/.npmrc
VOLUME /root/node/lib/node_modules

EXPOSE 3000

CMD ["nodemon"]