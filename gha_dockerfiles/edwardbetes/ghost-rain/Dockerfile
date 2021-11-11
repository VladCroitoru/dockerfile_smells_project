FROM node:14-bullseye-slim

RUN apt update && apt install -y --no-install-recommends bash curl ca-certificates gettext-base

ADD ./ghost /app
RUN npm install -g ghost-cli@latest

RUN cd /app && ln -s versions/4.16.0 current && envsubst < config.placeholder.json > config.production.json && envsubst < .ghost-cli-ph > .ghost-cli && cd current && npm install --production

WORKDIR /app
CMD cd /app && ghost run