FROM golang:alpine AS build-env

RUN apk update && apk add git

ADD server /build
WORKDIR /build
RUN go get -d ./...
RUN go build -o /soulcaster-server

FROM alpine

EXPOSE 80

COPY --from=build-env /soulcaster-server /server/soulcaster-server
COPY build /build

CMD ["/server/soulcaster-server", "-p", "80"]