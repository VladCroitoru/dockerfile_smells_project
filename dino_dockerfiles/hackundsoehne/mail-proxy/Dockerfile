FROM node:11-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN rm -rf node_modules && npm install && npm cache clean --force

EXPOSE 4567
CMD ["npm", "start"]
