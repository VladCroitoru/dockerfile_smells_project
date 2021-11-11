FROM node:alpine

WORKDIR /app

COPY package.json .

RUN set -xe && npm install --no-cache

COPY index.js .

ENTRYPOINT ["node"]
CMD ["index.js"]
