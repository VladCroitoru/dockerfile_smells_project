FROM node:16.6.0

WORKDIR /usr/src/app

COPY ./ ./

RUN npm ci -q && npm run build-prod && rm -rf src/ && npm ci -q --omit=dev

CMD ["node", "."]
