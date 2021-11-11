FROM mhart/alpine-node:latest

WORKDIR /src
ADD app.js .
ADD package.json .
RUN npm install

CMD ["node","app.js"]