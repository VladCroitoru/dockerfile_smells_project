FROM node:5.5.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app
RUN npm install

COPY . /usr/src/app
RUN npm run build

WORKDIR /usr/src/app/build

RUN npm i -g http-server


EXPOSE 8080

CMD ["http-server"]