FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y \
       gawk \
       git \
       build-essential \
       autoconf \
       automake \
       libtool \
       libncurses5 libncurses5-dev \
       gawk \
       libjpeg-dev \
       libz-dev \
       pkg-config \
       sqlite3 libsqlite3-dev \
       libcurl3 libcurl3-dev \
       libpcre++0 libpcre3-dev \
       libspeex-dev speex libspeexdsp-dev \
       libedit-dev \
       libldns-dev \
       erlang \
       wget \
       python-dev \
       libyaml-dev \
       gcj-jdk && \
    update-alternatives --set awk /usr/bin/gawk

RUN mkdir /opt/freeswitch && \
    cd /usr/src && \
    git clone https://freeswitch.org/stash/scm/fs/freeswitch.git && \
    cd freeswitch && \
    git checkout tags/v1.4.20

COPY modules.conf /usr/src/freeswitch/

RUN cd /usr/src/freeswitch && \
    ./bootstrap.sh && \
    ./configure --prefix=/opt/freeswitch --with-java=/usr/java/jdk1.6.0_16/include/ && \
    make && \
    make install && \
    make sounds-fr-install

RUN adduser --disabled-password  --quiet --system --home /opt/freeswitch --gecos "FreeSwitch Voice Platform" --ingroup daemon freeswitch && \
    adduser freeswitch audio && \
    chown -R freeswitch:daemon /opt/freeswitch && \
    chmod -R o-rwx /opt/freeswitch

USER freeswitch

CMD /opt/freeswitch/bin/freeswitch
