FROM node:alpine as builder
WORKDIR /app
COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn install
COPY ./ ./
RUN yarn build

FROM node:alpine
WORKDIR /app
COPY --from=builder /app/package.json ./
COPY --from=builder /app/yarn.lock ./
COPY --from=builder /app/dist ./dist
RUN yarn install --prod
CMD ["node", "./dist/index.js"]