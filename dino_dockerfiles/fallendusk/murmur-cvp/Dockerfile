FROM ubuntu:14.04
MAINTAINER Greg Helton <greg@fallendusk.com>

ENV MURMUR_ICE_HOST mumble
ENV MURMUR_ICE_PORT 6502
ENV MURMUR_CONNECT_URL mumble://localhost:64738
EXPOSE 5000


RUN apt-get update \
 && apt-get install -y python-flask python-zeroc-ice python-imaging

RUN mkdir -p /srv
WORKDIR /srv
ADD flaskcvp-2.5 /srv/flaskcvp
ADD Murmur.ice /usr/share/slice/Murmur.ice
ADD boot_flaskcvp.sh /srv/boot_flaskcvp.sh
RUN chmod 0755 /srv/boot_flaskcvp.sh

CMD ["/srv/boot_flaskcvp.sh"]
