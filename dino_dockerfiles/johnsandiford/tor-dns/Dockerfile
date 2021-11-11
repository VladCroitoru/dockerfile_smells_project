# run dns across tor in a container
#
# docker run -d \
#	--restart always \
#	-v /etc/localtime:/etc/localtime:ro \
#	-p 53/udp -p 53/tcp \
# 	--name tor-dns \
# 	johnsandiford/tor-dns
#
FROM alpine:latest
MAINTAINER John Sandiford <john@sandiford.net>

# Note: Tor is only in testing repo -> http://pkgs.alpinelinux.org/packages?package=emacs&repo=all&arch=x86_64
RUN apk update && apk add \
	tor \
	git \
	make \
	gcc \
	musl-dev \
	libc-dev \
	--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
	&& rm -rf /var/cache/apk/*

RUN mkdir /tor-dns && \
	cd tor-dns && \
	git clone https://github.com/jtRIPper/dns-tcp-socks-proxy.git && \
	cd dns-tcp-socks-proxy && \
	make

# expose dns port
EXPOSE 53/udp

# copy in our files
COPY torrc.default /etc/tor/torrc.default
COPY dns_proxy.conf /tor-dns/dns-tcp-socks-proxy/dns_proxy.conf
COPY resolv.conf /tor-dns/dns-tcp-socks-proxy/resolv.conf

# run dns-tcp-socks-proxy
# RUN /tor-dns/dns-tcp-socks-proxy/dns_proxy

# make sure files are owned by tor user
RUN chown -R tor /etc/tor

USER tor

# ENTRYPOINT [ "tor" ]
# CMD [ "-f", "/etc/tor/torrc.default" ]
