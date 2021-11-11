FROM alpine:latest as builder
RUN apk add -U --no-cache ca-certificates
FROM alpine:latest
ENV GODEBUG netdns=go
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ADD drone-mattermost /bin/
ENTRYPOINT ["/bin/drone-mattermost"]
