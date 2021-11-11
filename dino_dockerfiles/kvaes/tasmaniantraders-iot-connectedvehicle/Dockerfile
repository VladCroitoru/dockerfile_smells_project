FROM node:boron

WORKDIR /usr/src/app

COPY app.js /usr/src/app/
COPY package.json /usr/src/app/

ENV iothubconnectionstring your-iothubowner-connectionstring
ENV offlineMin 0
ENV offlineMax 1
ENV interval 15

RUN cd /usr/src/app && npm install

CMD [ "npm", "start" ]
