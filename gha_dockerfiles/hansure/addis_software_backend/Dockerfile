# Dockerfile
FROM node:10
WORKDIR /app
COPY  package.json /app
RUN npm install
COPY . /app
CMD node app.js
EXPOSE 8888
