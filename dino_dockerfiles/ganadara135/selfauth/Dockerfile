FROM node:8.1.2

MAINTAINER kcod <ganadara135@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
COPY package.json /usr/src/app/
RUN npm install && npm cache clean --force
COPY . /usr/src/app

EXPOSE  3000 1999 80

CMD [ "npm", "start" ]

#이미지생성 명령어
#docker build -t {원하는 이미지명} .   {. 마침표는 현재폴더위치에서를 의미}

#컨테이너  생성 명령어(윈도우환경에서 호스트폴더 연결하여 개발시)
#docker run --name myappc -p 3000:3000 -v d:\\mychain:/usr/src/app myapp node server.js
