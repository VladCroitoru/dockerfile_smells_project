FROM debian:jessie

ARG DEBIAN_FRONTEND=noninteractive
ARG WEBMIN_DEB_URL=http://prdownloads.sourceforge.net/webadmin/webmin_1.831_all.deb

RUN echo "Acquire::GzipIndexes \"false\"; Acquire::CompressionTypes::Order:: \"gz\";" >/etc/apt/apt.conf.d/docker-gzip-indexes \
  && echo root:pass | chpasswd \
  && apt-get update -q && apt-get install -yqq \
  wget \
  perl-base \
  libnet-ssleay-perl \
  openssl \
  libauthen-pam-perl \
  libpam-runtime \
  libapt-pkg-perl \
  libio-pty-perl \
  apt-show-versions \
  python

RUN wget -O webmin.deb $WEBMIN_DEB_URL \
  && chmod +x webmin.deb \
  && dpkg -i webmin.deb || true \
  && apt-get install -y -f

EXPOSE 10000

VOLUME ["/etc/webmin"]

CMD /usr/bin/touch /var/webmin/miniserv.log && /usr/sbin/service webmin restart && /usr/bin/tail -f /var/webmin/miniserv.log
