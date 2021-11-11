FROM navikt/node-express:12.2.0-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

ENV NODE_EXTRA_CA_CERTS /etc/ssl/ca-bundle.pem

COPY ./server/node_modules ./node_modules
COPY ./server/dist ./dist
COPY ./build ./build

EXPOSE 3000

ENTRYPOINT ["sh", "-c"]
CMD ["node dist/main.js"]
