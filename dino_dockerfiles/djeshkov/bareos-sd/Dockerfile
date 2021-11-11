FROM shoifele/bone-centos

MAINTAINER Dan Jeshkov <d.jeshkov@gmail.com>

ENV REFRESHED_AT="2016-08-19" \
    BAREOS_SD_CONF_FILE=bareos-sd.conf

RUN curl -Ls http://download.bareos.org/bareos/release/latest/CentOS_7/bareos.repo \
    > /etc/yum.repos.d/bareos.repo \
  && yum -y install \
    bareos-storage \
    sshfs \
    cifs-utils \
  && yum clean all

ADD rootfs /

EXPOSE 9103
VOLUME /storage
VOLUME /etc/bareos

CMD ["/init"]
