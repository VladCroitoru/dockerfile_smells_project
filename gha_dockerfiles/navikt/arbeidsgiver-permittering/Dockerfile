FROM navikt/node-express:14-alpine
ENV NODE_ENV production

WORKDIR /app
COPY server ./server
COPY build/ ./build

USER root
RUN chown -R apprunner:apprunner /app
USER apprunner

WORKDIR /app/server
RUN yarn install --frozen-lockfile

EXPOSE 3000
CMD ["node", "server.js"]
