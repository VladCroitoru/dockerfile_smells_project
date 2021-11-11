FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -q update \
    && apt-get install -qy \
      acl attr autoconf bison build-essential \
      debhelper dnsutils docbook-xml docbook-xsl flex gdb krb5-user \
      libacl1-dev libaio-dev libattr1-dev libblkid-dev libbsd-dev \
      libcap-dev libcups2-dev libgnutls-dev libjson-perl \
      libldap2-dev libncurses5-dev libpam0g-dev libparse-yapp-perl \
      libpopt-dev libreadline-dev perl perl-modules pkg-config \
      python-all-dev python-dev python-dnspython python-crypto \
      xsltproc zlib1g-dev git \
      avahi-daemon \
      avahi-utils \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

# clone and build samba. Based on this patch: https://github.com/samba-team/samba/pull/64
RUN cd /tmp \
    && git clone -b bz12380-full_fsync https://github.com/kevinanderson1/samba.git \
    && cd samba \
    && ./configure && make -j$(nproc) && make -j$(nproc) install \
    && cd /tmp \
    && rm -rf -- ./samba

# install s6-overlay init manager (https://github.com/just-containers/s6-overlay)
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

# install samba config
ADD ./smb.conf /usr/local/samba/etc/smb.conf

# set an upper limit on the reported vol size so that timemachine doesn't eat the entire disk
ENV TIMEMACHINE_MAX_VOL_SIZE_GB  750
ADD ./samba-dfree.sh /bin/samba-dfree.sh

# create a 'backup' user with password 'backup'
RUN (echo backup; echo backup) | /usr/local/samba/bin/smbpasswd -s -a backup

# install avahi (bonjour) announcer
ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf
ADD smb.service       /etc/avahi/services/smb.service

# s6 service scripts
ADD nmbd-run.sh         /etc/services.d/nmbd/run
ADD smbd-run.sh         /etc/services.d/smbd/run
ADD avahi-daemon-run.sh /etc/services.d/avahi-daemon/run

# s6 fix-attrs script
ADD 01-timemachine-data-dir /etc/fix-attrs.d/01-timemachine-data-dir

EXPOSE 137/udp 138/udp 139 445

CMD ["/init"]
