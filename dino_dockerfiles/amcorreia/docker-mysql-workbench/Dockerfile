#
# DESCRIPTION:    Image with Mysql Workbench
# TO_BUILD:       docker build -t amcorreia/docker-mysql-workbench .
# TO_RUN:         docker run -d --rm -it  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --name workbench amcorreia/docker-mysql-workbench

FROM debian:jessie

MAINTAINER  Alessandro Madruga Correia <mutley.sandro@gmail.com>

# To avoid problems with Dialog and curses wizards
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends ca-certificates apt-transport-https wget apt-utils lsb-release && \
    apt-key adv --keyserver pgp.mit.edu --recv-keys 5072E1F5 && \
    wget -O /tmp/mysql.deb https://dev.mysql.com/get/mysql-apt-config_0.8.6-1_all.deb && \
    dpkg -i /tmp/mysql.deb && \
    rm /tmp/mysql.deb && \
    apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends mysql-workbench mysql-client && \
    apt-get remove --yes --quiet ca-certificates apt-transport-https wget apt-utils lsb-release && \
    apt-get clean --yes && \
    rm -rf -- /var/lib/apt/lists/*

VOLUME ~/.mysql/workbench/
VOLUME /backups

CMD /usr/bin/mysql-workbench
