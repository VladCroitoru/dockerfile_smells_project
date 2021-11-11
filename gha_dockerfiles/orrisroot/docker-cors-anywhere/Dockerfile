FROM docker.io/library/node:14-buster AS build-env
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --production

FROM gcr.io/distroless/nodejs-debian10:14
WORKDIR /app
COPY --from=build-env /app/node_modules /app/node_modules
EXPOSE 8080
CMD ["node_modules/cors-anywhere/server.js"]
