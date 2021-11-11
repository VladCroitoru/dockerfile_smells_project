FROM node:14.16.1 AS node-builder

ARG CHECKOUT_PATH=webapp

WORKDIR /build
COPY ./${CHECKOUT_PATH}/package*.json ./
RUN npm ci --only=production
COPY ./${CHECKOUT_PATH} ./
RUN npm run build

WORKDIR /dist
RUN cp -r /build/build ./

FROM golang:1.16.3 AS golang-builder

ARG CHECKOUT_PATH=server

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64

WORKDIR /build
COPY ./${CHECKOUT_PATH}/go.mod ./
COPY ./${CHECKOUT_PATH}/go.sum ./
RUN go mod download
COPY ./${CHECKOUT_PATH} ./
RUN go build -o main ./

WORKDIR /dist
RUN cp /build/main ./
RUN cp /build/configs/config.prod.json ./

FROM scratch

LABEL author="parkgang[Kyungeun Park]<ruddms936@naver.com>"
LABEL version="0.1.0"

ENV GO_ENV=production

WORKDIR /webapp
COPY --from=node-builder /dist/build ./build

WORKDIR /server
COPY --from=golang-builder /dist/main ./
COPY --from=golang-builder /dist/config.prod.json ./configs/config.prod.json

EXPOSE 8080

ENTRYPOINT ["/server/main"]