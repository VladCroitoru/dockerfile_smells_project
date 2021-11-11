FROM ubuntu:16.04

RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
  wget \
  dialog \
  openssh-client \
  software-properties-common \
  dnsmasq \
  dnsutils \
  net-tools \
  sudo \
  rsyslog \
  openssh-server \
  unzip \
  tzdata

VOLUME ["/opt/zimbra"]

EXPOSE 22 25 465 587 110 143 993 995 80 443 8080 8443 7071

RUN echo "tzdata tzdata/Areas select Asia\ntzdata tzdata/Zones/Asia select Jakarta" > /tmp/tz ; debconf-set-selections /tmp/tz; rm /etc/localtime /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

COPY opt /opt/

COPY etc /etc/

CMD ["/bin/bash", "/opt/start.sh", "-d"]
