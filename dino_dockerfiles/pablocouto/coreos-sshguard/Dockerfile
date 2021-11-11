FROM alpine:3.2

RUN apk add --update \
    iptables \
    ip6tables \
    sshguard \
 && rm -fr /var/cache/apk/*

ENTRYPOINT ["/usr/sbin/sshguard"]
