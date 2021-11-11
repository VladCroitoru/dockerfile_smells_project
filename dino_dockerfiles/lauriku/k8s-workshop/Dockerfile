FROM node:9

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN yarn install

EXPOSE 3000

ENTRYPOINT ["yarn", "start"]
