FROM node:14-alpine

RUN mkdir /app
WORKDIR /app

ADD package.json yarn.lock /app/
RUN yarn
ADD . /app

EXPOSE 3000

CMD ["yarn", "start"]
