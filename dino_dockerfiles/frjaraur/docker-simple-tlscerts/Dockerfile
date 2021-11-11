FROM alpine
MAINTAINER frjaraur@gmail.com
RUN apk --update add openssl
WORKDIR /certs
VOLUME /certs
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["help"]
