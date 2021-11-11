FROM node

WORKDIR /usr/src/app

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

RUN npm install

COPY . /usr/src/app
ENTRYPOINT npm start