FROM node:latest as js-build-stage
WORKDIR /app
COPY ./rss-frontend/package.json ./
COPY ./rss-frontend/yarn.lock ./
RUN yarn install
COPY ./rss-frontend/ .
RUN yarn run build

FROM golang:1.17-alpine as go-build-stage
RUN mkdir /src
COPY ./ /src/
WORKDIR /src
RUN go build ./cmd/main.go

FROM alpine:3.14.2 as final-stage
RUN mkdir /app
WORKDIR /app
COPY --from=go-build-stage /src/main /app/main
RUN mkdir /app/dist
COPY --from=js-build-stage /app/dist /app/dist
CMD /app/main
