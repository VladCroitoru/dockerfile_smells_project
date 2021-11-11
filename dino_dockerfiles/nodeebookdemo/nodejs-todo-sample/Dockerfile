FROM node:8.9-alpine
WORKDIR /usr/src/app
COPY . .
RUN npm install && (cd static && npm install)
EXPOSE 3000
CMD node app.js
