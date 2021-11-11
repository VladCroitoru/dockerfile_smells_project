# DOCKER-VERSION 18.01.0-ce

FROM node:8.9.4-alpine

# Bundle app source
ADD . /webapp

# Install app dependencies
RUN cd /webapp; npm install;

EXPOSE 9000
CMD ["node","/webapp/index.js"]
