FROM alpine:latest

WORKDIR /app
COPY bchttpd .

ENV GIN_MODE=release

EXPOSE 8080/tcp

VOLUME /var/www

CMD ["/app/bchttpd"]