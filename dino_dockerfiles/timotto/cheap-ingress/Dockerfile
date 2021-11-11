FROM node:8-alpine AS build

ADD . /build

WORKDIR /build

RUN yarn install && \
    yarn run test && \
    yarn run tsc && \
    rm -rf node_modules/ && \
    yarn install --production=true

FROM node:8-alpine AS runtime

COPY --from=build /build /app

RUN apk update && apk add -y iptables iproute2

WORKDIR /app

VOLUME /data
ENV NODES 169.254.123.125 169.254.123.126 169.254.123.127
ENV INTERFACE eth0
ENV IPPOOL_PREFIX 169.254.123.
ENV IPPOOL_HOSTMIN 100
ENV IPPOOL_HOSTMAX 200
ENV DOMAIN cheap-ingress.local
ENV DEBUG util cheap-ingress:*
ENV PORT 80
ENV STATE_FILENAME /data/state.json

CMD node dist