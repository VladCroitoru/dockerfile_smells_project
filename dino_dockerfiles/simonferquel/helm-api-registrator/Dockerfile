FROM golang:1.10.0-alpine3.7 AS build
WORKDIR /go/src/github.com/simonferquel/helm-api-registrator
COPY main.go /go/src/github.com/simonferquel/helm-api-registrator/
COPY vendor /go/src/github.com/simonferquel/helm-api-registrator/vendor/
RUN go build

FROM alpine:3.7
RUN apk --update upgrade && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY --from=build /go/src/github.com/simonferquel/helm-api-registrator/helm-api-registrator /helm-api-registrator
ENTRYPOINT [ "/helm-api-registrator" ]