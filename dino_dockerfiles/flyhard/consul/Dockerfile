FROM flyhard/debian-consul
MAINTAINER Per Abich <per.abich@gmail.com>

RUN apt-get update && apt-get install -y ca-certificates && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD entrypoint.sh /
EXPOSE 8500 8400 8300 8600 8301 8302 8301/udp 8302/udp 8600/udp
VOLUME ["/var/lib/consul"]

ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
