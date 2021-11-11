# vim: set et:

FROM        centos:7.2.1511
MAINTAINER  Christian Lindig <christian.lindig@citrix.com>

# set up yum repo
COPY    files/RPM-GPG-KEY-Citrix-6.6 \
        /etc/pki/rpm-gpg/RPM-GPG-KEY-Citrix-6.6

# Build requirements
RUN     yum install -y \
            gcc \
            gcc-c++ \
            git \
            make \
            mock \
            rpm-build \
            rpm-python \
            sudo \
            yum-utils \
            epel-release \
            tig \
            tmux \
            vim \
            wget \
            which \
            http://download.opensuse.org/repositories/home:/ocaml/CentOS_7/x86_64/aspcud-1.9.0-2.1.x86_64.rpm \
            http://download.opensuse.org/repositories/home:/ocaml/CentOS_7/x86_64/clasp-3.0.1-4.1.x86_64.rpm \
            http://download.opensuse.org/repositories/home:/ocaml/CentOS_7/x86_64/gringo-4.3.0-10.1.x86_64.rpm

# OCaml in XS is slightly older than in CentOS
RUN     sed -i "/gpgkey/a exclude=ocaml*" \
        /etc/yum.repos.d/Cent* /etc/yum.repos.d/epel*

# override these when building the container
# docker build --build-arg uid=$(id -u) --build-arg gid=$(id -g) .
ARG uid=1000
ARG gid=1000

RUN echo 'builder ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/builder \
&&  chmod 440 /etc/sudoers.d/builder \
&&  chown root:root /etc/sudoers.d/builder \
&&  sed -i.bak 's/^Defaults.*requiretty//g' /etc/sudoers \
&&  groupadd -f -g $gid builder \
&&  useradd -d /home/builder -u $uid -g builder -m -s /bin/bash builder \
&&  passwd -l builder \
&&  usermod -G mock builder \
&&  :

WORKDIR /home/builder
COPY    files/build build
COPY    files/rpmmacros .rpmmacros
COPY    files/yum-setup yum-setup

RUN     ./yum-setup \
&&      chown -R builder:builder /home/builder

# now become user builder
USER    builder
ENV     HOME /home/builder
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["exec /bin/bash -l"]



