FROM node:slim

# Create app directory
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN npm install
ENTRYPOINT npm start