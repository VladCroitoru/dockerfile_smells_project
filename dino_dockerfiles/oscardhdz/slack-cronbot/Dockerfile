FROM node:alpine

RUN mkdir -p /home/cronbot

WORKDIR /home/cronbot

COPY .  .

RUN npm install

ENV NODE_ENV=prod

CMD ["npm", "start"]
