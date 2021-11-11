FROM node:lts

WORKDIR /usr/app

COPY . .
RUN yarn
RUN yarn dist

CMD ["yarn", "start"]