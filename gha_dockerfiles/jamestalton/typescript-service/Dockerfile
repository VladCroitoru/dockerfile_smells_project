FROM --platform=${BUILDPLATFORM:-linux/amd64} node:14-alpine as builder
RUN apk add --no-cache python make g++ openssl
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm ci
RUN npm run postinstall
COPY . /app/
RUN npm run build
RUN npm run test
RUN npm run lint
RUN npm run check
RUN rm -rf node_modules
RUN npm ci --only=production
RUN npm i pino-zen

FROM --platform=${TARGETPLATFORM:-linux/amd64} node:14-alpine
ENV NODE_ENV production
WORKDIR /app
COPY --from=builder /app/certs /app/certs
RUN chown -R node /app/certs
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /app/build /app/
USER node
CMD ["node", "lib/main"]