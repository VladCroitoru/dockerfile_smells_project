FROM node:12.16.1 AS builder
LABEL stage=intermediate
WORKDIR /app
COPY . .
RUN yarn install
RUN yarn build
#only install required package needed in prod to keep small package size
RUN rm -rf ./node_modules
RUN yarn install --production

# copy built application to runtime image
FROM node:12.16.1-slim
WORKDIR /app
COPY --from=builder /app/config ./config
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

ENV NODE_ENV production
ENTRYPOINT [ "node", "dist/app.js" ]
