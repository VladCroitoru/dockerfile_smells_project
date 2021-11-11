FROM alpine

LABEL maintainer="Vitaly Kovalyshyn"

RUN apk add --no-cache tftp-hpa

EXPOSE 69/udp

ENTRYPOINT ["in.tftpd"]

CMD ["-L", "--verbose", "-u", "root", "--secure", "--create", "/tftp"]
