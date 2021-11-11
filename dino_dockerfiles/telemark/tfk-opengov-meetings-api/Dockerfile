FROM mhart/alpine-node:10 as base
RUN apk add --update git && rm -rf /var/cache/apk/*
WORKDIR /usr/src
COPY package.json package-lock.json /usr/src/
RUN npm i --production
COPY . .

FROM mhart/alpine-node:base-10
WORKDIR /usr/src
COPY --from=base /usr/src .
CMD ["node", "standalone.js"]