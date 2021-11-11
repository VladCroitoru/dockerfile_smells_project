FROM node:11-alpine
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/
# Hash the content
RUN (find -type f -exec md5sum {} \; | md5sum | cut -d' ' -f1) > hash
# Install app dependencies
RUN npm install

VOLUME /usr/src/app/storage

EXPOSE 80
CMD [ "npm", "start" ]
