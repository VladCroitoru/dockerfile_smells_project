FROM node:10.15.0-alpine

ENV NODE_ENV=production

WORKDIR /cpu_test

COPY server.js package.json package-lock.json ./

RUN npm install --production

EXPOSE 8888
USER node

CMD ["node", "--abort-on-uncaught-exception", "./server.js"]
