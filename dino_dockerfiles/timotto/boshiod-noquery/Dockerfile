FROM node:10-alpine AS build

ADD . /build

WORKDIR /build

RUN yarn install && \
    yarn run tsc && \
    rm -rf node_modules/ && \
    yarn install --production=true

FROM node:10-alpine AS runtime

COPY --from=build /build /app

WORKDIR /app

ENV PORT 8080

CMD node dist