FROM mhart/alpine-node:6.1.0

ENV ZK_STATUS_ZK_URL tcp://localhost:2181
ENV ZK_STATUS_LISTEN_PORT 8080
ENV ZK_STATUS_ZK_TIMEOUT 1000
ENV NODE_ENV production

RUN mkdir /zkstatus && addgroup zkstatus && adduser zkstatus -D -G zkstatus && chown -R zkstatus /zkstatus

WORKDIR /zkstatus

USER zkstatus

COPY package.json .

RUN npm install

COPY index.js .

EXPOSE $ZK_STATUS_LISTEN_PORT

CMD ["npm", "start"]
