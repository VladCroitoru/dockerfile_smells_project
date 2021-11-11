FROM alpine
RUN apk --update add unbound
#RUN /usr/sbin/unbound-anchor -a /etc/unbound/root.key
COPY unbound.conf /etc/unbound/unbound.conf
COPY localrecords.conf /etc/unbound/localrecords.conf
COPY entrypoint.sh /entrypoint.sh
EXPOSE 53/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["unbound","-d"]
