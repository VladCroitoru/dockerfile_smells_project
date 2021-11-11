FROM alpine:edge

# install common packages
RUN apk update && apk upgrade && \
	apk add haproxy curl iptables &&\
    curl -o /usr/bin/confd -sSL \
        https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 && \
    chmod +x /usr/bin/confd

COPY entrypoint.sh /usr/bin/entrypoint.sh
COPY confd/ /etc/confd/

VOLUME ["/var/lib/haproxy"]

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD [""]

EXPOSE 80 443