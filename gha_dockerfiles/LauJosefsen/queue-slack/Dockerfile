FROM node:14.18-buster

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN  npm install -g ts-node
RUN npm install --save

COPY . .

CMD [ "node", "--loader", "ts-node/esm", "src/index.ts"]