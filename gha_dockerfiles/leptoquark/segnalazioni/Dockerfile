FROM node:12.15.0

RUN mkdir -p /usr/src/segnalazioni

COPY dist/segnalazioni /usr/src/segnalazioni/dist/segnalazioni
COPY ssl /usr/src/segnalazioni/ssl

COPY authMiddleware.js /usr/src/segnalazioni/
COPY serverdata.json /usr/src/segnalazioni/
COPY server.js /usr/src/segnalazioni/server.js
COPY deploy-package.json /usr/src/segnalazioni/package.json

WORKDIR /usr/src/segnalazioni

RUN npm install

EXPOSE 8080

CMD ["node", "server.js"]