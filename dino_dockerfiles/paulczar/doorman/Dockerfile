# Creates openstack common base image
#
# Author: Paul Czarkowski
# Date: 08/24/2014

FROM node

ADD . /doorman
WORKDIR /doorman

RUN mv /doorman/conf.example.js /doorman/conf.js

# install your application's dependencies
RUN npm install

# replace this with your application's default port
EXPOSE 8888

# replace this with your main "server" script file
CMD [ "node", "app.js" ]