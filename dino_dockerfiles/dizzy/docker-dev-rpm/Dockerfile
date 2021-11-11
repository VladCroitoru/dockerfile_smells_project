FROM mattdm/fedora:f19

COPY sipxcom.repo /etc/yum.repos.d/sipxcom.repo

RUN yum -y install epel-release; yum clean all && yum -y install git \
  make \
  autoconf \
  automake \
  dart-sdk \
  rpm-build \
  libxslt \
  mock \
  sudo \
  createrepo \
  thttpd \
  libtool \
  openssl-devel \
  java-1.7.0-openjdk \
  java-1.7.0-openjdk-devel \
  ruby \
  ruby-devel \
  rubygems \
  wget && \
  gem install fpm && rm -rf /etc/yum.repos.d/sipxcom.repo && yum clean all && \
  useradd -m sipx && usermod -G mock sipx && echo "sipx    ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

VOLUME ["/home/sipx/sipxcom"]

ADD ./build_rpm.sh /build_rpm.sh
RUN chmod +x /build_rpm.sh

USER sipx
ENV HOME /home/sipx
WORKDIR /home/sipx/sipxcom
ENTRYPOINT ["/build_rpm.sh"]
