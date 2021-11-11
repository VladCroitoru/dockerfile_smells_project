FROM alpine:3.14

RUN apk add --no-cache iptables

COPY azure-iptables-rule.sh /

RUN chmod +x azure-iptables-rule.sh

ENTRYPOINT /azure-iptables-rule.sh
