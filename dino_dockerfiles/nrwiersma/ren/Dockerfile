FROM alpine:latest as builder

RUN apk --no-cache --update add ca-certificates

FROM scratch

COPY --from=builder /etc/ssl/certs /etc/ssl/certs
COPY ren /ren

ENV PORT "80"

EXPOSE 80
CMD ["./ren", "server"]
