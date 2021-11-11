FROM golang:1.17-alpine AS go_builder
RUN mkdir /build
ADD go.mod go.sum main.go /build/
ADD api/ /build/api/
WORKDIR /build
RUN go build

FROM node:14 as node_builder
ENV NODE_ENV=production
RUN mkdir /client
ADD client/ /client/
WORKDIR /client
RUN yarn install
RUN yarn build

FROM alpine
RUN adduser -S -D -H -h /app appuser
USER appuser
COPY --from=go_builder /build/go-react /app/
COPY --from=node_builder /client/build/ /app/public
WORKDIR /app
CMD ["./go-react"]