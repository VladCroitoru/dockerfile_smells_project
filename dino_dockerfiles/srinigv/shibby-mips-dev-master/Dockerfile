FROM debian:wheezy-backports

### upgrade to latest and install SSH
ENV DEBIAN_FRONTEND noninteractive
RUN dpkg --add-architecture i386
RUN apt-get update && \
 apt-get upgrade -y && \
 apt-get install -y openssh-server


### config SSH
RUN mkdir /var/run/sshd && \
 echo 'root:shibby' | chpasswd && \
 sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
 sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]


### install tomatousb build essentials
RUN \
 apt-get install -y build-essential curl wget apt-utils locales && \
 apt-get install -y autoconf git-core libncurses5 libncurses5-dev m4 \
  bison flex libstdc++6-4.4-dev g++-4.4 g++ libtool sqlite gcc binutils \
  patch bzip2 make gettext unzip zlib1g-dev libc6 gperf sudo \
  automake automake1.9 lib32stdc++6 gawk g++-4.4-multilib git gitk \
  autopoint shtool autogen mtd-utils gcc-multilib gconf-editor \
  lib32z1-dev pkg-config libssl-dev libxml2-dev libelf1:i386 \
  intltool libglib2.0-dev libstdc++5 texinfo dos2unix xsltproc \
  libnfnetlink0 libcurl4-openssl-dev libgtk2.0-dev libnotify-dev \
  libevent-dev mc re2c mlocate libglib2.0-data:i386 shared-mime-info:i386 \
  autoconf2.13 autoconf-archive gnu-standards groff texlive nettle-dev
WORKDIR /root
ADD extra_packages /root/extra_packages
RUN dpkg -i /root/extra_packages/automake_1.13.2-1ubuntu1_all.deb && \
 apt-get install -y net-tools vim ctags
RUN rm -rf /root/extra_packages
# RUN apt-get autoclean -y && apt-get autoremove -y


### make /bin/sh symlink to bash instead of dash
RUN echo "dash dash/sh boolean false" | debconf-set-selections && \
 DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash


### locale settings
RUN dpkg-reconfigure locales && \
 locale-gen C.UTF-8 && \
 /usr/sbin/update-locale LANG=C.UTF-8 && \
 echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \
 locale-gen
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8


### UTC timezone
RUN echo "UTC" > /etc/timezone && \
 dpkg-reconfigure -f noninteractive tzdata


### tomato user and utils for tomatousb repo
RUN useradd -ms /bin/bash tomato && \
 echo 'tomato:shibby' | chpasswd && \
 adduser tomato sudo
ADD get_shibby.sh /bin/
ADD copy_source_to_compile.sh /bin/

