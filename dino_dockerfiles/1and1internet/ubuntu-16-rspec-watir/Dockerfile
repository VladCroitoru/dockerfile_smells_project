FROM ubuntu:xenial
MAINTAINER nick.campion@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files/ /
RUN \
  apt-get -y update && \
  apt-get -y install xvfb ruby ruby-rspec ruby-ffi git firefox=45.0.2+build1-0ubuntu1 wget ca-certificates openssl locales && \
  gem install watir watir-ng headless && \
  locale-gen en_GB.utf8 && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/* && \
  cd /usr/share/ca-certificates/ && \
  mkdir 1and1 && \
  cd 1and1 && \
  wget http://pub.pki.1and1.org/pukirootca1.crt && \
  wget http://pub.pki.1and1.org/pukiissuingca1.crt && \
  openssl x509 -noout -in pukirootca1.crt -fingerprint -sha256 >a && \
  echo "SHA256 Fingerprint=6B:DE:2B:46:BA:BF:52:1E:09:45:41:16:AE:CD:73:65:DE:79:EB:D9:49:FE:B3:9C:E9:F1:1C:2B:46:60:C0:CD" | diff a - && \
  openssl x509 -noout -in pukiissuingca1.crt -fingerprint -sha256 >b && \
  echo "SHA256 Fingerprint=E1:99:91:7B:7F:DE:02:AF:00:AC:D0:65:0D:7B:E0:42:2A:A6:8E:E4:C1:53:BA:12:EF:15:3D:DB:62:A2:9A:DC" | diff b - && \
  rm a b && \
  cd .. && \
  ls -1 1and1/* >>  /etc/ca-certificates.conf && \
  update-ca-certificates
ENV \
  LC_ALL=en_GB.UTF-8 \
  LANG=en_GB.UTF-8 \
  LANGUAGE=en_GB.UTF-8
EXPOSE 7055
CMD /bin/bash
