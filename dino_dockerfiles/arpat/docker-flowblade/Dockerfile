# Flowblade Linux Video Editor
# https://github.com/jliljebl/flowblade
#
# Tested with https://github.com/jliljebl/flowblade/releases/download/v1.14/flowblade-1.14.0-1_all.deb
#


FROM debian:testing
MAINTAINER Arun Patel <arunsmtp@gmail.com>

ADD https://github.com/jliljebl/flowblade/releases/download/v1.16/flowblade-1.16.0-1_all.deb /flowblade.deb

RUN apt-get update && apt-get install -y \
      --no-install-recommends \
	apt-transport-https \
        ca-certificates \
        procps \
        dbus \
        dbus-x11 \
     && dpkg -i '/flowblade.deb' || /bin/true \
     && apt-get -y -f install \
     && dpkg -i '/flowblade.deb' \
     && apt-get -y auto-remove

WORKDIR /workdir

ENTRYPOINT ["/usr/bin/flowblade"]
