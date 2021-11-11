FROM alpine
ARG release_tag=v0.1-alpha
ADD https://github.com/twilfong/dex-example-app/releases/download/${release_tag}/dex-example-app /go/bin/dex-example-app
RUN chmod 755 /go/bin/dex-example-app
RUN apk --no-cache add ca-certificates
ENTRYPOINT ["/go/bin/dex-example-app"]
