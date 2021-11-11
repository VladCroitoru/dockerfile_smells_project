FROM node:13

WORKDIR /app

COPY server /app
RUN yarn install

COPY build /app/build

CMD ["node", "./serve.js"]

EXPOSE 3000