FROM mhart/alpine-node:6

ADD . /app
WORKDIR /app

RUN npm i --production

CMD ["npm", "start"]
