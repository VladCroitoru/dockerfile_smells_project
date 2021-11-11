FROM debian:wheezy

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
	apt-get install -q -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" openswan procps kmod \
	iptables lsof \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 500/udp 4500/udp

CMD ["/usr/bin/tail", "-f", "/dev/null"]
