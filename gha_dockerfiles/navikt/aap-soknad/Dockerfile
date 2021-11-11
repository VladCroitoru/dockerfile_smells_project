FROM navikt/node-express:14-alpine
ENV NODE_ENV production

WORKDIR /app
COPY server/dist/ ./server
COPY build/ ./build


USER root
RUN chown -R apprunner:apprunner /app

WORKDIR /app
EXPOSE 3000
CMD ["node", "server/index.js"]