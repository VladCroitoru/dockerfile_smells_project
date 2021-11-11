# Build sorces in the development mode
FROM node:12-alpine as base

WORKDIR /app

COPY yarn.lock package.json ./
RUN yarn install --frozen-lockfile --production

ENV NODE_ENV=production

FROM base as builder

RUN yarn install --frozen-lockfile --production=false
RUN yarn global add @nestjs/cli

COPY . .

RUN yarn build:all

FROM base

COPY --from=builder /app/dist /app/dist
COPY . .

EXPOSE 3000

CMD yarn start:prod
