FROM mhart/alpine-node:4

RUN apk add --no-cache ruby && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npm install -g nodemon
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

EXPOSE 80

CMD [ "npm", "start" ]
