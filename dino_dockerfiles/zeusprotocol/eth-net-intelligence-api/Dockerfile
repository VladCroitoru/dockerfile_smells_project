FROM node:9

WORKDIR /app

COPY . .

RUN yarn install --no-progress

ENV NODE_ENV production
ENV RPC_HOST localhost
ENV RPC_PORT RPC_PORT
ENV LISTENING_PORT 30303
ENV WS_SERVER wss://rpc.ethstats.net
ENV WS_SECRET secret
ENV VERBOSITY 2

CMD ["node", "app.js"]
