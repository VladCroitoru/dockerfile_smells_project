FROM node:17-alpine AS builder

RUN apk update
RUN apk add python3 g++ make

WORKDIR /usr/src/app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

RUN npm run build
RUN npm prune --production

FROM node:17-alpine

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/dist ./dist
COPY --from=builder /usr/src/app/assets ./assets
COPY --from=builder /usr/src/app/node_modules ./node_modules

CMD [ "node", "dist/main.js" ]