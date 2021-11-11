FROM node:latest

RUN npm install -g jshint@~2.9.1
RUN npm install -g bower@~1.7.2
RUN npm install -g nodemon@~1.9.1
RUN npm install -g gulp-cli@~1.2.0
RUN npm install -g bcrypt

VOLUME /var/www/app
WORKDIR /var/www/app

RUN npm config set prefix /root/node
VOLUME /root/node/lib/node_modules

EXPOSE 3000

CMD ["nodemon",  "-L", "/var/www/app/lib/app.js",  "-w .",  "-w node_modules"]
