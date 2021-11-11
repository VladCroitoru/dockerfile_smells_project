FROM turbulent/heap-base:2.0.3
MAINTAINER Marc Alloul	<malloul@turbulent.ca>

ENV heap-telegraf 1.0.0
ENV TELEGRAF_VERSION 1.3.0

RUN set -ex && \
    for key in \
        05CE15085FC09D18E99EFB22684A14CF2582E0C5 ; \
    do \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
        gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \
    done

RUN apt-get update && apt-get install wget -y && \
    wget -q https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}-1_amd64.deb.asc && \
    wget -q https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}-1_amd64.deb && \
    gpg --batch --verify telegraf_${TELEGRAF_VERSION}-1_amd64.deb.asc telegraf_${TELEGRAF_VERSION}-1_amd64.deb && \
    dpkg -i telegraf_${TELEGRAF_VERSION}-1_amd64.deb && \
    rm -f telegraf_${TELEGRAF_VERSION}-1_amd64.deb* && \
    apt-get remove --purge wget -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -y clean

EXPOSE 8125/udp 8092/udp 8094

ADD telegraf.conf.tmpl /systpl
ADD run.sh /run.sh

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/run.sh"]
