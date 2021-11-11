FROM navikt/node-express:14

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

WORKDIR /var/server
COPY server/ ./server
COPY build/ ./build

USER root
RUN chown -R apprunner /var/server/build
RUN chown -R apprunner /var/server/server
USER apprunner

WORKDIR /var/server/server
RUN yarn install --frozen-lockfile

EXPOSE 3000
ENTRYPOINT ["node", "server.js"]
