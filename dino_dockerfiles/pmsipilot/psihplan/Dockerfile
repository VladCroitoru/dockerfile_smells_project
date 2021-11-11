FROM node:6 as builder

ENV NODE_ENV=development

RUN npm install -g grunt

COPY . /app
WORKDIR /app

RUN npm install && \
    grunt

FROM node:6

ENV NODE_ENV=production

EXPOSE 3700

COPY --from=builder /app/server /app/server
COPY --from=builder /app/package.json /app/package.json

WORKDIR /app

RUN cp server/config/config.js.dist server/config/config.js && \
    npm install && \
    npm cache clean

ENTRYPOINT ["node", "/app/server/index.js"]
