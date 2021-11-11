FROM node:12.18.1-alpine as builder
ADD . .
RUN yarn install --skip-integrity-check --non-interactive \
    && yarn build

FROM node:12.18.1-alpine
ENV NODE_ENV production
WORKDIR /app
ADD . /app
RUN yarn install --production --skip-integrity-check --non-interactive
COPY --from=builder dist/index.js /app/index.js
ENTRYPOINT ["/app/bin/heuristicalert.js"]
