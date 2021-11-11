FROM node:9-alpine

ADD . /app
WORKDIR /app
RUN npm install -g yarn
RUN yarn

EXPOSE 80
CMD ["node", "server.js"]