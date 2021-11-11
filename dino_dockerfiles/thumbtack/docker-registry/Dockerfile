FROM registry
MAINTAINER Eric Naeseth <eric@thumbtack.com>

ADD ./configure.sh /docker-registry/configure.sh
ADD ./config.yml /docker-registry/config.yml

CMD cd /docker-registry && ./configure.sh && ./run.sh
