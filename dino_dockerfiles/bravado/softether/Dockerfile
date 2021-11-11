FROM debian:8 AS builder

ENV VERSION v4.29-9680-rtm-2019.02.28

RUN apt-get update &&\
	apt-get -y -q install iptables gcc make curl

RUN curl -L http://www.softether-download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Server/64bit_-_Intel_x64_or_AMD64/softether-vpnserver-${VERSION}-linux-x64-64bit.tar.gz \
	| tar -xz -C /usr/local/

RUN cd /usr/local/vpnserver && make i_read_and_agree_the_license_agreement

FROM debian:8

RUN apt-get update &&\
	apt-get -y --no-install-recommends -q install iptables uml-utilities &&\
	apt-get clean && \
	rm -rf /var/cache/apt/* /var/lib/apt/lists/*

COPY --from=builder /usr/local/vpnserver /usr/local/vpnserver/

ADD docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh

WORKDIR /app

VOLUME /app

EXPOSE 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp 500/udp 4500/udp

CMD [ "server" ]

ENTRYPOINT ["/docker-entrypoint.sh"]

