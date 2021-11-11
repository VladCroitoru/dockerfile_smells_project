
FROM node

RUN npm install -g --silent nodal

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

EXPOSE 3000

CMD ["nodal","s"]

