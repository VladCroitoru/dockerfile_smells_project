FROM haproxy:1.6.3
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
CMD sleep 5 && haproxy -f /usr/local/etc/haproxy/haproxy.cfg
