FROM alpine

LABEL maintainer="Carlos Sanz <carlos.sanzpenas@gmail.com>"

LABEL org.label-schema.vendor = "Personal" \
      org.label-schema.name = "Syslog-NG" \
      org.label-schema.version = "3.30.1-r0" \
      org.label-schema.docker.cmd = "docker run -p 514:514 sanzcarlos/syslog-ng:alpine" \
      org.label-schema.url = "https://pkgs.alpinelinux.org/packages?name=syslog-ng" \
      org.label-schema.build-date = "2021-02-02"

RUN apk update && \
    apk upgrade && \
    apk add syslog-ng && \
    rm -rf /var/cache/apk/*

ADD https://raw.githubusercontent.com/sanzcarlos/syslog-ng/master/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf

EXPOSE 514/udp
EXPOSE 601/tcp
#EXPOSE 6514/tcp

ENTRYPOINT ["/usr/sbin/syslog-ng", "-F"]
