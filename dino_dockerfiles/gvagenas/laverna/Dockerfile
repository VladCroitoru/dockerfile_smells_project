FROM node:4-onbuild

RUN npm install -g bower
RUN npm install -g gulp
RUN cd /usr/src/app
RUN npm install
RUN bower install --allow-root
CMD [ "gulp" ]

EXPOSE 9000
