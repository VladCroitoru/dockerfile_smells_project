FROM alpine:3.2
MAINTAINER Mikhail Simin <mikhail@nextdoor.com>

RUN apk add --update bash python py-pip py-yaml ca-certificates

RUN mkdir -p /app /app/zk_monitor
ADD ./* /app/
ADD ./zk_monitor /app/zk_monitor
RUN cd /app; python setup.py install
ADD entrypoint.sh /

EXPOSE 80

RUN chmod +x /entrypoint.sh
ENTRYPOINT "/entrypoint.sh"
