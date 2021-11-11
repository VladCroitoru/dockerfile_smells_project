FROM --platform=$BUILDPLATFORM node:lts-alpine as builder

WORKDIR /nodeaas
COPY . .

RUN set -ex && \
    npm ci && \
    npm run build

FROM node:lts-alpine

WORKDIR /nodeaas

COPY --from=builder /nodeaas/dist .
COPY nodeaas.config.js .

RUN set -ex && \
    apk --no-cache add ca-certificates

CMD ["node", "/nodeaas/index.js", "-c", "/nodeaas/nodeaas.config.js"]
