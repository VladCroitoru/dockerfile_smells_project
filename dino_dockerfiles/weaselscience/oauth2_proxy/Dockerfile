FROM alpine:3.5

RUN apk --no-cache add ca-certificates && update-ca-certificates

COPY ./oauth2_proxy /usr/local/bin/oauth2_proxy

RUN ["chmod", "+x", "/usr/local/bin/oauth2_proxy"]

CMD ["oauth2_proxy"]
