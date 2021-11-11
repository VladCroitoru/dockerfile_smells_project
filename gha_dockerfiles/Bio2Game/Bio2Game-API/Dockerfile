FROM node:16.6.1 as builder
WORKDIR /app
COPY . .

RUN npm i \
  && node ace build --production \
  && cd build \
  && npm ci --production

FROM node:16.6.1
WORKDIR /app
COPY --from=builder /app/build .

EXPOSE 6002
CMD node server.js
