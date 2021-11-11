FROM pihole/pihole:latest
RUN apt update && apt install -y unbound

COPY ./lighttpd-external.conf /etc/lighttpd/external.conf
COPY ./unbound-pihole.conf /etc/unbound/unbound.conf.d/pi-hole.conf
COPY ./start_unbound_and_s6_init.sh start_unbound_and_s6_init.sh

RUN mkdir -p /var/log/unbound \
  && chown unbound:unbound /var/log/unbound/ \
  && touch /var/log/unbound/unbound.log \
  && chown unbound:unbound /var/log/unbound/unbound.log

RUN chmod +x start_unbound_and_s6_init.sh
ENTRYPOINT ./start_unbound_and_s6_init.sh
