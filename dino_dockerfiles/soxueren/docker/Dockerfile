FROM docker:latest

RUN apk add --no-cache curl tar bash procps

ADD server.crt /server.crt
RUN cat /server.crt >> /etc/ssl/certs/ca-certificates.crt

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sh"]
