FROM node:16-alpine

WORKDIR /usr/src/app

COPY package.json .
COPY yarn.lock .
RUN yarn install

COPY . .

RUN yarn prisma generate
RUN yarn build

RUN npx cpx "src/**/*.graphql" ./dist

ENV NODE_ENV=production
ENV NODE_OPTIONS=--unhandled-rejections=throw
ENV LOG_LEVEL=info

RUN chmod +x .infra/docker/entrypoint.sh

EXPOSE 4000

ENTRYPOINT [".infra/docker/entrypoint.sh"]

CMD node dist/index.js