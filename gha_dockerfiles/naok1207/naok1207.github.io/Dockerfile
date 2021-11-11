FROM node:12.22-alpine
RUN apk update && \
  apk add bash vim

RUN mkdir /app

WORKDIR /app
COPY package.json .
RUN yarn install

COPY . /app

EXPOSE 3000

CMD ["yarn", "run", "start"]