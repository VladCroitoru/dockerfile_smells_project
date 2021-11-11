FROM node:alpine as BUILD_IMAGE

RUN apk add git
RUN git clone https://github.com/innatical/layers-backend.git /layers-backend

WORKDIR /layers-backend

ARG SENTRY_AUTH_TOKEN
RUN yarn install --frozen-lockfile

WORKDIR /app

COPY package.json yarn.lock ./

# install dependencies
RUN apk add libc6-compat
RUN yarn install --frozen-lockfile

COPY . .

# build
RUN yarn build

# remove dev dependencies
RUN npm prune --production

FROM node:alpine

WORKDIR /app

# copy from build image
COPY --from=BUILD_IMAGE /app/package.json ./package.json
COPY --from=BUILD_IMAGE /app/node_modules ./node_modules
COPY --from=BUILD_IMAGE /app/.next ./.next
COPY --from=BUILD_IMAGE /app/public ./public

EXPOSE 3000
CMD ["yarn", "start"]
