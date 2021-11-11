FROM golang:alpine as build
ARG VERSION=latest
RUN apk add --update git
WORKDIR /go/src/github.com/Kaitsh/herrnhuter-daily
COPY .    .
RUN go get -v -d ./...
RUN CGO_ENABLED=0 GOOS=linux go build -v -ldflags "-X main.version=$VERSION" -a -installsuffix cgo -o server-docker-v$VERSION .

FROM scratch
LABEL Maintainer=kaitsh@d-git.de
ARG VERSION=latest
COPY --from=build /go/src/github.com/Kaitsh/herrnhuter-daily/server-docker-v$VERSION /run/server
COPY --from=build /go/src/github.com/Kaitsh/herrnhuter-daily/public /run/public
COPY --from=build /go/src/github.com/Kaitsh/herrnhuter-daily/assets /run/assets
WORKDIR /run

EXPOSE 3333

CMD [ "./server" ]

