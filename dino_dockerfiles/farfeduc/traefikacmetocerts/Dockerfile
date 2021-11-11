FROM node:alpine
MAINTAINER Farfeduc

RUN npm i -g nodemon

WORKDIR /app
COPY . /app

CMD ["nodemon", "--watch", "", "index.js"]