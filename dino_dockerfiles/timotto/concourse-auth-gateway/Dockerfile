FROM node:12-alpine AS build

ADD . /build

WORKDIR /build

RUN npm install && \
    npm run test && \
    npm run tsc && \
    rm -rf node_modules/ && \
    npm install --production=true

FROM node:12-alpine AS runtime

COPY --from=build /build /app

WORKDIR /app

ENV PORT 3001

ENV STATE_FILENAME /state.json

CMD node dist
