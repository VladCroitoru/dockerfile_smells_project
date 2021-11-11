FROM node:12.16.1-alpine as builder

WORKDIR /opt/dev-portal

RUN apk add --no-cache -t build-dependencies git make gcc g++ python libtool autoconf automake \
  && cd $(npm root -g)/npm \
  && npm config set unsafe-perm true \
  && npm install -g node-gyp

COPY package.json package-lock.json* /opt/dev-portal/
RUN npm install

COPY docs /opt/dev-portal/docs
RUN npm run build

FROM node:12.16.1-alpine
WORKDIR /opt/dev-portal

RUN mkdir -p /opt/dev-portal/docs/.vuepress/dist

COPY --from=builder /opt/dev-portal/node_modules /opt/dev-portal/node_modules
COPY --from=builder /opt/dev-portal/package.json /opt/dev-portal/package.json
COPY --from=builder /opt/dev-portal/package-lock.json /opt/dev-portal/package-lock.json
COPY --from=builder /opt/dev-portal/docs/.vuepress/dist /opt/dev-portal/docs/.vuepress/dist

RUN npm prune --production

CMD [ "npm", "run", "serve" ]
