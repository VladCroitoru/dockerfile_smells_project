FROM alpine:latest

RUN apk --no-cache add curl
COPY dummy /usr/bin/dummy

EXPOSE 8080

CMD ["/usr/bin/dummy"]
