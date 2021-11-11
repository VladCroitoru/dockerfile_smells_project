
FROM node:14-alpine as builder

ENV NODE_ENV build

# USER node
WORKDIR /usr/src/app

COPY . .

RUN npm ci \
    && npm run build

# ---

FROM node:14-alpine

ENV NODE_ENV production

# USER node
WORKDIR /usr/src/app


COPY --from=builder /usr/src/app/package*.json /usr/src/app/
COPY --from=builder /usr/src/app/dist/ /usr/src/app/dist/

RUN npm ci

CMD ["node", "dist/main.js"]
