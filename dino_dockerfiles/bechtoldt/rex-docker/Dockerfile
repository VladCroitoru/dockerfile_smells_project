FROM debian:wheezy
MAINTAINER Arnold Bechtoldt <mail@arnoldbechtoldt.com>

RUN export DEBIAN_FRONTEND=noninteractive; \
  apt-get update -qq && \
  apt-get install -yV -o DPkg::Options::=--force-confold \
      apt-transport-https \
      ssh \
      wget && \
  \
  apt-get clean && \
  rm -rf \
    /tmp/* \
    /var/cache/apt/* \
    /var/cache/debconf/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

RUN ln -s /usr/bin/eu-readelf /usr/bin/readelf

RUN wget -O - https://rex.linux-files.org/DPKG-GPG-KEY-REXIFY-REPO | apt-key add -
RUN echo "deb https://rex.linux-files.org/debian/ wheezy rex" >> /etc/apt/sources.list

RUN export DEBIAN_FRONTEND=noninteractive; \
  apt-get update -qq && \
  apt-get install -yV -o DPkg::Options::=--force-confold \
    cpanminus \
    elfutils \
    gcc \
    libnet-openssh-perl \
    libnet-sftp-foreign-perl \
    libpar-packer-perl \
    make \
    rex && \
  \
  apt-get clean && \
  rm -rf \
    /tmp/* \
    /var/cache/apt/* \
    /var/cache/debconf/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

RUN cpanm -n -l /usr/local/perl https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-OpenSSH-0.62.tar.gz

CMD export PERL5LIB=/usr/local/perl/lib/perl5:${PERL5LIB} && \
  /bin/bash -l
