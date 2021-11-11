FROM node:lts as dependencies
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

FROM node:lts as builder
WORKDIR /usr/src/app
COPY . .
COPY --from=dependencies /usr/src/app/node_modules ./node_modules
RUN yarn build

FROM node:lts as runner
WORKDIR /usr/src/app
ENV NODE_ENV production
COPY --from=builder /usr/src/app/.env.local ./
COPY --from=builder /usr/src/app/.next ./.next
COPY --from=builder /usr/src/app/node_modules ./node_modules
COPY --from=builder /usr/src/app/package.json ./package.json

EXPOSE 3000
CMD ["yarn", "start"]
