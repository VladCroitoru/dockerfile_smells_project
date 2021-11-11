FROM node:6.4.0
MAINTAINER niceilm@naver.com

WORKDIR /opt
RUN git clone https://github.com/nasa/openmct.git

WORKDIR /opt/openmct
RUN npm install
RUN ./node_modules/bower/bin/bower install --allow-root
RUN ./node_modules/gulp/bin/gulp.js install

EXPOSE 8080
CMD npm start
