FROM timhaak/base:latest
MAINTAINER kurri@glappet.com

ENV SICKGEAR_VERSION="master"

RUN apt-get -q update && \
    apt-get install -qy --force-yes python-cheetah python-openssl && \
    curl -L https://github.com/SickGear/SickGear/tarball/${SICKGEAR_VERSION} -o SickGear.tgz && \
    tar -xvf SickGear.tgz -C /  && \
    mv /SickGear-SickGear-* /SickGear/ && \
    rm  /SickGear.tgz && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

VOLUME ["/config", "/data"]

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

EXPOSE 8081

CMD ["/start.sh"]
