FROM node:alpine


RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN yarn install

EXPOSE 3333

CMD ["yarn", "dev"]