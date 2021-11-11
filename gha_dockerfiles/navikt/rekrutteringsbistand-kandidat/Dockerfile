FROM navikt/node-express:12.2.0-alpine

WORKDIR /usr/src/app

COPY build/ build/
COPY server/ ./

RUN npm ci

EXPOSE 8080

CMD ["node", "server.js"]