FROM node:12-alpine AS build

ADD . /build

WORKDIR /build

RUN npm install && \
    npm run test && \
    npm run tsc && \
    npm install --production

FROM node:12-alpine AS runtime

COPY --from=build /build /app

WORKDIR /app

ENV PORT 8080

ENV DBURL http://localhost:5894

ENV DEBUG mqtt-http-gateway:*

CMD node dist
