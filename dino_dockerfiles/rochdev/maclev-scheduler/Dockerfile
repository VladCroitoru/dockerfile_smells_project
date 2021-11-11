FROM mhart/alpine-node:4

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npm install -g nodemon
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

CMD [ "node", "." ]
