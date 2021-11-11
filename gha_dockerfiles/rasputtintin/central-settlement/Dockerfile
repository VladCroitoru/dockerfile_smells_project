FROM node:10.15.3-alpine as builder

WORKDIR /opt/central-settlement

RUN apk add --no-cache -t build-dependencies git make gcc g++ python libtool autoconf automake \
    && cd $(npm root -g)/npm \
    && npm config set unsafe-perm true

COPY package.json package-lock.json* /opt/central-settlement/

RUN npm install

COPY config /opt/central-settlement/config
COPY src /opt/central-settlement/src
COPY README.md /opt/central-settlement

FROM node:10.15.3-alpine
WORKDIR /opt/central-settlement

COPY --from=builder /opt/central-settlement .

RUN npm prune --production

# Create empty log file & link stdout to the application log file
RUN mkdir ./logs && touch ./logs/combined.log
RUN ln -sf /dev/stdout ./logs/combined.log

EXPOSE 3007
CMD node src/server.js
