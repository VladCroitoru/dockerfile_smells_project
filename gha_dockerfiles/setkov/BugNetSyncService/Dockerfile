FROM golang:alpine as builder
RUN apk update && apk add ca-certificates && apk add tzdata
WORKDIR /go/src/app
COPY . .
# Static build required so that we can safely copy the binary over.
RUN CGO_ENABLED=0 go install -ldflags '-extldflags "-static"'

FROM scratch
COPY --from=builder /go/bin/BugNetSyncService /BugNetSyncService
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

ENV TZ Europe/Moscow
ENTRYPOINT ["/BugNetSyncService"]
