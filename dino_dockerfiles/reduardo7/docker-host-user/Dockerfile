FROM phusion/baseimage:latest

MAINTAINER Eduardo Daniel Cuomo <reduardo7@gmail.com> <eduardo.cuomo.ar@gmail.com>

RUN apt-get update && \
  apt-get -y install sudo && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /
ADD init-user.sh /init-user.sh
RUN chmod a+x /init-user.sh

ENTRYPOINT ["/init-user.sh"]
