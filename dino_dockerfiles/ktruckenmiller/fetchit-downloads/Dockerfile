FROM node:8.1.3
RUN mkdir -p /project
COPY package.json /project
WORKDIR /project
RUN npm install
COPY . /project
RUN npm build
EXPOSE 4000
ENTRYPOINT node app.js
