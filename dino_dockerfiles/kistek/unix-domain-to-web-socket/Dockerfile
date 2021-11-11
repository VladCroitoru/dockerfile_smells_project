FROM node:8-alpine

ENTRYPOINT ["node", "/app/src/index.js"]

COPY package* /app/

RUN npm --prefix=/app install --production

COPY src /app/src
