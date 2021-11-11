FROM golang:1.17.1-alpine3.14 as build

WORKDIR /go/src/github.com/dpattmann/furby

COPY . /go/src/github.com/dpattmann/furby

RUN apk add -U --no-cache curl jq

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -installsuffix 'static' /go/src/github.com/dpattmann/furby/cmd/furby/furby.go

FROM scratch

EXPOSE 8443

COPY --from=build /go/src/github.com/dpattmann/furby/furby /bin/furby

ENTRYPOINT [ "/bin/furby" ]
