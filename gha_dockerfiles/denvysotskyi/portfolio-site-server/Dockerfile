FROM node

WORKDIR /app

COPY package.json /app

RUN yarn install

COPY . .

ENV PORT 3000

EXPOSE $PORT

CMD [ "node", "start" ]
