FROM node:14 as builder
WORKDIR /usr/src
COPY package.json ./
COPY tsconfig.json ./
COPY yarn.lock ./
COPY src ./src
RUN yarn && yarn add typescript -g
RUN yarn build

FROM node:14 as runtime
WORKDIR /usr/src 
ENV NODE_ENV=production
COPY --from=builder /usr/src/package.json ./package.json
COPY --from=builder /usr/src/yarn.lock ./yarn.lock
COPY --from=builder /usr/src/build ./build
RUN yarn install --frozen-lockfile

EXPOSE 8080
ENTRYPOINT [ "yarn","start" ]