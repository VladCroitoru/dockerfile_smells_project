FROM ubuntu:14.04

# https://www.digitalocean.com/community/tutorials/how-to-run-an-unrealircd-chat-server-on-debian-7
# https://www.unrealircd.org/faq#29

MAINTAINER  Erik Osterman "e@osterman.com"

ENV UNREALIRCD_VERSION 3.2.10.5
ENV UNREALIRCD_CONF /etc/unrealircd/default.conf

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/src

RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/01buildconfig && \
    echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/01buildconfig && \
    echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf.d/01buildconfig  && \
    echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/01buildconfig && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential curl libssl-dev ca-certificates && \
    apt-get clean && \
    curl -s --location https://www.unrealircd.org/downloads/Unreal$UNREALIRCD_VERSION.tar.gz | tar xz && \
    cd Unreal$UNREALIRCD_VERSION && \
    ./configure \
      --enable-ssl=/etc/ssl/localcerts/ \
      --with-zip \
      --with-showlistmodes \
      --with-listen=5 \
      --with-dpath=/etc/unrealircd/ \
      --with-spath=/usr/bin/unrealircd \
      --with-nick-history=2000 \
      --with-sendq=3000000 \
      --with-bufferpool=18 \
      --with-permissions=0600 \
      --with-fd-setsize=1024 \
      --enable-dynamic-linking && \
    make && \
    make install && \
    mkdir -p /usr/lib64/unrealircd/modules && \
    echo "" > /etc/unrealircd/ircd.motd && \
    echo "" > /etc/unrealircd/ircd.rules && \
    mv /etc/unrealircd/modules/* /usr/lib64/unrealircd/modules/ && \
    chown nobody:nogroup -R /etc/unrealircd && \
    chmod 0755 /usr/bin/unrealircd /usr/lib64/unrealircd/modules/* && \
    mkdir /var/log/unrealircd/ && \
    chown nobody:nogroup /var/log/unrealircd/ && \
    rmdir /etc/unrealircd/modules && \
    apt-get -y remove build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/src/* /etc/unrealircd/unrealircd.conf

ADD default.conf /etc/unrealircd/default.conf
ADD openssl.cnf /etc/unrealircd/openssl.cnf
ADD start /start
ADD conf.d/ /etc/unrealircd/conf.d/

WORKDIR /
USER nobody
EXPOSE 6667
EXPOSE 6697
EXPOSE 7000

ENTRYPOINT ["/start"]
