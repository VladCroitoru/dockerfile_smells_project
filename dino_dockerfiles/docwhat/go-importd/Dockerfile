FROM alpine:latest AS certificates
RUN apk add --no-cache ca-certificates

FROM scratch AS release
ENV COLUMNS 80
EXPOSE 80
COPY --from=certificates /etc/ssl/ /etc/ssl/
COPY go-importd /go-importd
ENTRYPOINT ["/go-importd"]
