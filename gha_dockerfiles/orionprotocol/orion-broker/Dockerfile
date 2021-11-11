FROM node:14-alpine

WORKDIR /usr/src/app

COPY . .

#WORKDIR broker-frontend
#
#RUN npm install
#
#RUN npm run build

WORKDIR /usr/src/app

RUN npm install

RUN npm run build

RUN mkdir dist/data
RUN cp config.template.json dist/data/config.json
RUN cp src/logo.png dist/logo.png
RUN cp src/icon.png dist/icon.png

WORKDIR dist

CMD [ "node", "main.js" ]