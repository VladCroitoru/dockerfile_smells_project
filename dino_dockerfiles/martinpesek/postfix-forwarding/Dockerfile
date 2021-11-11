FROM alpine:3.5

MAINTAINER Martin Pešek <pesek.dev@gmail.com>

# Variables to use when creating a container from this image:
# HOSTNAME - server's hostname - preferably FQDN one, example: awesome-server.somedomain.com
# DOMAINS - virtual alias domains that you want to forward mails for, example: example.com somedomain.com
# EMAILS - rules for forwarding, example: @example.com myemail@gmail.com\n@somedomain.com myemail@gmail.com\n

RUN apk --no-cache add postfix ca-certificates supervisor rsyslog bash

COPY assets/postfix.sh /postfix.sh
COPY assets/supervisord.conf /etc/supervisord.conf
COPY assets/rsyslog.conf /etc/rsyslog.conf

RUN chmod +x /postfix.sh

EXPOSE 25

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
