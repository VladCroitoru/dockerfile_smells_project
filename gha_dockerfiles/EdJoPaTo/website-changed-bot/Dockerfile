FROM docker.io/library/node:16-alpine AS builder
WORKDIR /build

COPY package.json package-lock.json tsconfig.json ./
RUN npm ci

COPY source source
RUN node_modules/.bin/tsc


FROM docker.io/library/node:16-alpine AS packages
WORKDIR /build
COPY package.json package-lock.json ./
RUN npm ci --production


FROM docker.io/library/node:16-alpine
ENV NODE_ENV=production
RUN apk upgrade --no-cache \
	&& apk add --no-cache bash git

WORKDIR /app
VOLUME /app/persistent
VOLUME /app/users
VOLUME /app/websites

COPY gitconfig /root/.gitconfig
COPY package.json ./
COPY --from=packages /build/node_modules ./node_modules
COPY --from=builder /build/dist ./

HEALTHCHECK --interval=5m \
    CMD bash -c '[[ $(find . -maxdepth 1 -name ".last-successful-run" -mmin "-25" -print | wc -l) == "1" ]]'

CMD node -r source-map-support/register index.js
