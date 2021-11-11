FROM golang:1.11-stretch AS builder

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN cd /usr/bin && wget -O dep https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 && chmod a+x dep

RUN mkdir -p /go/src/github.com/bitly/oauth2_proxy
WORKDIR /go/src/github.com/bitly/oauth2_proxy

COPY Gopkg.toml Gopkg.lock ./

RUN dep ensure -vendor-only
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s -w" -a -installsuffix cgo -o oauth2_proxy

FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /app/

COPY --from=builder /usr/local/bin/dockerize /usr/local/bin/dockerize
COPY --from=builder /go/src/github.com/bitly/oauth2_proxy/oauth2_proxy  .

COPY /templates /templates

EXPOSE 4180

ENTRYPOINT ["/usr/local/bin/dockerize", "-template", "/templates/config.tmpl:/app/config"]
CMD ["/app/oauth2_proxy", "-config=/app/config"]

