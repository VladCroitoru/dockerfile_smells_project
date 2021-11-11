FROM alpine:latest
ENV DNSCRYPT_VERSION 2.0.4
ENV CONF_FILE /config/dnscrypt-proxy.toml

RUN apk add --no-cache dnsmasq wget ca-certificates && \
	wget -q https://github.com/jedisct1/dnscrypt-proxy/releases/download/$DNSCRYPT_VERSION/dnscrypt-proxy-linux_x86_64-$DNSCRYPT_VERSION.tar.gz && \
	tar -xzf dnscrypt-proxy-linux_x86_64-$DNSCRYPT_VERSION.tar.gz && \
	mkdir -p /opt/dnscrypt-proxy /config && \
	mv /linux-x86_64/* /opt/dnscrypt-proxy && \
	chown -R root:root /opt/dnscrypt-proxy && \
	chmod ugo+x /opt/dnscrypt-proxy/dnscrypt-proxy && \
	rm -R /linux-x86_64

COPY dnsmasq.conf /config/dnsmasq.conf
COPY extra_hosts /config/extra_hosts
COPY dnscrypt-proxy.toml /config/dnscrypt-proxy.toml

EXPOSE 2053/tcp 2053/udp

VOLUME ["/config"]

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

