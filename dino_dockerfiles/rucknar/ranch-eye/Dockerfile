FROM haproxy:1.6
MAINTAINER Ed Marshall <ed.marshall@infinityworks.com>

ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

CMD exec haproxy -db -f /usr/local/etc/haproxy/haproxy.cfg

EXPOSE 9104
