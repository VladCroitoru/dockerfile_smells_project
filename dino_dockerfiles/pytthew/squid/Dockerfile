FROM debian:stretch-slim
RUN apt update -qq && export DEBIAN_FRONTEND=noninteractive \
 && apt install -y squid \
 && ln -sf /usr/share/zoneinfo/Europe/Budapest /etc/localtime \
 && dpkg-reconfigure -f noninteractive tzdata \
 && apt-get clean && rm -rf /var/lib/apt/lists/
ADD squid /etc/init.d/squid
RUN chmod 755 /etc/init.d/squid
ENTRYPOINT ["/etc/init.d/squid","start"]
