# example build:
# docker build -t myapp -f Dockerfile.prod . --build-arg DB_ENDPOINT=mongodb://<ip address>:27017/myapp

FROM node:12-buster

RUN apt update && apt install -y tini

ARG DB_ENDPOINT
ARG APP_PORT=3000

EXPOSE $APP_PORT

ENV DB_ENDPOINT=$DB_ENDPOINT
ENV APP_PORT=$APP_PORT

USER node

WORKDIR /home/node

COPY package*.json ./

RUN npm i

ENV NODE_ENV=production

COPY --chown=node:node . .

RUN npm run build

ENTRYPOINT ["tini", "--"]

CMD ["node", "dist/index.js"]
