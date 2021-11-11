FROM node:16

ENV HOME /root

WORKDIR /root

COPY . .

WORKDIR /root/frontend

RUN npm install

EXPOSE $PORT

CMD npm run start

