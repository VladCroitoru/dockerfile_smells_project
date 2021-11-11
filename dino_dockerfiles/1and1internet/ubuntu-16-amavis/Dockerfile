FROM docker.io/1and1internet/ubuntu-16:latest
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
  apt-get update && \
  apt-get -o Dpkg::Options::=--force-confdef -y install gettext-base spamassassin clamav clamav-daemon libauthen-sasl-perl libdbi-perl libnet-dns-perl libmail-dkim-perl libnet-ldap-perl libsnmp-perl libmail-spf-perl pyzor razor arj bzip2 cabextract cpio file gzip lhasa nomarch pax unrar-free unzip zip zoo lzop p7zip rpm altermime ripole lrzip rsyslog && \
  apt-get install -y libmime-tools-perl libio-stringy-perl \
                     libunix-syslog-perl libnet-server-perl \
                     db-util libberkeleydb-perl libarchive-zip-perl && \
  wget https://amavisd.de.postfix.org/amavisd-new-2.11.1.tar.bz2 && \
    tar xvf amavisd-new-2.11.1.tar.bz2 && \
    cd amavisd-new-2.11.1 && \
    useradd -d /var/amavis amavis && \
    mkdir -p /var/amavis /var/amavis/tmp /var/amavis/var /var/amavis/db /var/amavis/home && \
    chown -R amavis:amavis /var/amavis && \
    chmod -R 750 /var/amavis && \
    cp amavisd /usr/local/sbin && \
    chown root /usr/local/sbin/amavisd && \
    chmod 755  /usr/local/sbin/amavisd && \
    cp amavisd.conf /etc/ && \
    chown root:amavis /etc/amavisd.conf && \
    chmod 640 /etc/amavisd.conf && \
    mkdir /var/virusmails && \
    chown amavis:amavis /var/virusmails && \
    chmod 750 /var/virusmails && \
    sed -i "s/daemon_group = 'vscan'/daemon_group = 'amavis'/" /etc/amavisd.conf && \
    sed -i "s/daemon_user  = 'vscan'/daemon_user = 'amavis'/" /etc/amavisd.conf && \
  adduser clamav amavis && \
  adduser amavis clamav && \
  apt-get -y clean && \
  mkdir /var/run/clamav/ && \
  chown clamav:clamav /var/run/clamav/ && \
  sed -i -e 's/AllowSupplementaryGroups false/AllowSupplementaryGroups true/g' /etc/clamav/clamd.conf && \
  sed -i -e 's/Foreground false/Foreground true/g' /etc/clamav/clamd.conf && \
  chmod 0444 /etc/logrotate.d/logrotate && \
  chmod +x /usr/sbin/updater.sh /usr/local/bin/logrotated.sh && \
  chown -R debian-spamd:debian-spamd /etc/spamassassin/ && \
  chown -R debian-spamd:debian-spamd /var/lib/spamassassin/ && \
  rm -rf /var/lib/apt/lists/* && \
  chmod -R 0755 /hooks
RUN \
  sed -i "s/# .myhostname.*/\$myhostname = \"amavis\" . \$ENV{'DOMAIN'};/" /etc/amavisd.conf
ENV DOMAIN=example.com \
    ENABLE_RAZOR_AND_PYZOR=0 \
    SMTP_IP=127.0.0.1
EXPOSE 10024
