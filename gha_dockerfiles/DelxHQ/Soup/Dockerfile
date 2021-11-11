FROM ghcr.io/delxhq/node-gyp-images:latest

COPY . /app

WORKDIR /app

RUN npm i
RUN npm run build

RUN rm -rf src

CMD ["npm", "run", "start:prod"]
