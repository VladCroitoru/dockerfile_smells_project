FROM progrium/busybox:latest
MAINTAINER Alan LaMielle <alan.lamielle@gmail.com>

RUN opkg-install curl bind-tools
ADD http://stedolan.github.io/jq/download/linux64/jq /usr/local/bin/
RUN chmod 0755 /usr/local/bin/jq

VOLUME ["/etc/env.d"]

ADD consul-bootstrap /bin/
ADD rethinkdb-bootstrap /bin/
ADD discover /bin/
