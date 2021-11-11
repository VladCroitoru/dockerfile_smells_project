FROM debian:jessie
MAINTAINER support-staff@lists.grid5000.fr

RUN apt-get update
RUN apt-get -y install build-essential devscripts fakeroot
RUN apt-get -y install gem2deb ruby

VOLUME ["/sources"]

ADD docker_entrypoint.sh /entrypoint.sh
RUN chmod o+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

