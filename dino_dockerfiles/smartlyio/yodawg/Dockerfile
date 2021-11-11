FROM ubuntu:xenial

ENV LANG "en_US.UTF-8"
ENV ADDPACKAGES "vim locales-all"

RUN set-ex; \
    apt-get update; \
    apt-get install --assume-yes --no-install-recommends \
      build-essential \
      ca-certificates \
      debootstrap \
      git \
      iproute2 \
      lxc \
      lxc-templates \
      lxctl \
      sudo \
      wget \
    ;

RUN set -ex; \
    wget --no-check-certificate https://releases.hashicorp.com/vagrant/2.0.3/vagrant_2.0.3_x86_64.deb -O /tmp/vagrant_2.0.3_x86_64.deb; \
    dpkg -i /tmp/vagrant_2.0.3_x86_64.deb; \
    apt-get install -f;

RUN set -ex; \
    vagrant plugin install vagrant-lxc; \
    git clone https://github.com/obnoxxx/vagrant-lxc-base-boxes.git /tmp/vagrant-lxc-base-boxes;

WORKDIR /tmp/vagrant-lxc-base-boxes

RUN set -ex; \
    sed -i 's/#!\/bin\/bash/#!\/bin\/bash -x/' mk-debian.sh common/download.sh common/package.sh debian/vagrant-lxc-fixes.sh debian/install-extras.sh common/utils.sh; \
    sed -i 's/lxc-attach -n/lxc-attach --elevated-privileges -n/' common/utils.sh;

COPY ./build-lxc-vagrant-box.sh /tmp/

CMD [ "/tmp/build-lxc-vagrant-box.sh", "xenial" ]
