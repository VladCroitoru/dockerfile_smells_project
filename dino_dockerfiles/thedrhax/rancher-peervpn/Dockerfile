FROM thedrhax/peervpn

MAINTAINER Dmitry Karikh <the.dr.hax@gmail.com>

RUN apk add --no-cache docker

ADD run.sh /
ENTRYPOINT ["/run.sh"]
CMD ["/usr/local/bin/peervpn", "/peervpn.conf"]
