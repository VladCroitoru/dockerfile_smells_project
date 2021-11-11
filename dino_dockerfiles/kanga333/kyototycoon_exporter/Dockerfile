
FROM golang:1.8.3-alpine3.6 as build
RUN apk add --no-cache make git
RUN go get github.com/kanga333/kyototycoon_exporter
RUN cd /go/src/github.com/kanga333/kyototycoon_exporter && make build

FROM alpine:3.6
COPY --from=build /go/src/github.com/kanga333/kyototycoon_exporter/kyototycoon_exporter /
EXPOSE 9306
ENTRYPOINT ["/kyototycoon_exporter"]