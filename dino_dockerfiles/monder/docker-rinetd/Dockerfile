FROM ubuntu

RUN apt-get update
RUN apt-get install -y rinetd
VOLUME ["/etc/rinetd.conf"]

CMD /usr/sbin/rinetd -f -c /etc/rinetd.conf
