FROM node:boron

RUN mkdir /app

COPY . /app/

WORKDIR /app/

RUN npm install
RUN npm run build

EXPOSE 4444

CMD [ "node", "/app/bin/ap-npm", "serve", "--config=/ap-npm/config.json"]
