FROM node:14-alpine3.13

RUN mkdir -p /home/node/server/node_modules && chown -R node:node /home/node/server
WORKDIR /home/node/server

COPY package.json yarn.* ./
USER node
RUN yarn

COPY --chown=node:node . .

RUN yarn build

CMD ["yarn", "start"]
EXPOSE 3333