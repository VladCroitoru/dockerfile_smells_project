FROM node:latest

COPY . /usr/src/app
WORKDIR /usr/src/app/server
RUN npm install --production
ENTRYPOINT ["node", "runner.js"]
EXPOSE 8888
