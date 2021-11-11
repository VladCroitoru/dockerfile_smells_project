FROM alpine:edge
RUN apk upgrade --no-cache \
 && apk add --no-cache supervisor bash jq curl iptables ip6tables iproute2 ipset \
 && echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
 && apk add --no-cache bird
ADD files /
ENV BGP_AS=65534 \
    BGP_PREFIXES= \
    BGP_NEIGHBORS= \
	MANAGED_ROUTES=static
CMD ["/boot.sh"]
HEALTHCHECK --interval=5s --timeout=15s --start-period=300s --retries=6 CMD /healthcheck.sh
