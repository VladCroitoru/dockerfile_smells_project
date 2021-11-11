FROM debian:latest
MAINTAINER Hongan Li <hongli@redhat.com>
# install binary and remove cache
RUN apt-get update \
    && apt-get install -y procps curl net-tools dnsutils tcpdump iperf smcroute \
    && rm -rf /var/lib/apt/lists/*
COPY omping /usr/local/bin/omping
COPY myscript.sh /usr/local/bin/myscript.sh
RUN chmod +x /usr/local/bin/omping
RUN chmod +x /usr/local/bin/myscript.sh
CMD ["/usr/local/bin/myscript.sh"]
