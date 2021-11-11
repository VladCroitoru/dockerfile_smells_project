FROM node:7

RUN mkdir /home/node/OSCWeb
ADD . /home/node/OSCWeb/
WORKDIR /home/node/OSCWeb/

RUN npm install

CMD npm start

EXPOSE 8000
