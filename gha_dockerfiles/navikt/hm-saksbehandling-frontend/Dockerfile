FROM navikt/node-express:14-alpine

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
ENV TZ="Europe/Oslo"

WORKDIR /app

COPY server/node_modules/ node_modules/
COPY /dist dist/

EXPOSE 3000

ENTRYPOINT [ "/entrypoint.sh", "node --max-http-header-size=16000 /app/dist/server/server.js" ]
