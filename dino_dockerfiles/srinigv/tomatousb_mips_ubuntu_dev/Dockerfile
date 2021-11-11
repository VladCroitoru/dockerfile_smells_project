FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y openssh-server
RUN mkdir /var/run/sshd && echo 'root:shibby-mips' | chpasswd && \
    sed -i 's|^PermitRootLogin\s+.*|PermitRootLogin yes|' /etc/ssh/sshd_config && \
    sed -i 's|session\s*required\s*pam_loginuid.so|session optional pam_loginuid.so|g' /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN apt-get install -y build-essential wget apt-utils locales
RUN apt-get install -y autoconf m4 bison flex g++ libtool sqlite gcc g++ binutils \
    patch bzip2 make gettext unzip zlib1g-dev libc6 gperf sudo automake groff \
    lib32stdc++6 libncurses5 libncurses5-dev gawk gitk zlib1g-dev autopoint shtool \
    autogen mtd-utils gcc-multilib gconf-editor lib32z1-dev pkg-config libssl-dev \
    automake1.11 libxml2-dev intltool libglib2.0-dev libstdc++5 texinfo dos2unix \
    xsltproc libnfnetlink0 libcurl4-openssl-dev libxml2-dev libgtk2.0-dev \
    libnotify-dev libevent-dev mc git git-core texlive nettle-dev
RUN apt-get install -y libelf1:i386 re2c mlocate libglib2.0-data:i386 \
    shared-mime-info:i386 autoconf2.13 autoconf-archive gnu-standards
# RUN apt-get install -y libstdc++6-4.4-dev g++-4.4

WORKDIR /root
ADD extra_packages /root/extra_packages
RUN dpkg -i /root/extra_packages/automake_1.13.2-1ubuntu1_all.deb
RUN dpkg -i /root/extra_packages/automake_1.14.1-2ubuntu1_all.deb
RUN apt-get install -y net-tools
RUN apt-get remove -y bison libbison-dev
RUN dpkg -i /root/extra_packages/libbison-dev_2.7.1.dfsg-1_amd64.deb
RUN dpkg -i /root/extra_packages/bison_2.7.1.dfsg-1_amd64.deb
RUN apt-get install -y vim ctags
RUN rm -rf /root/extra_packages

# RUN apt-get autoclean -y && apt-get autoremove -y

# make /bin/sh symlink to bash instead of dash:
RUN echo "dash dash/sh boolean false" | debconf-set-selections && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash

# locales
RUN locale-gen en_US.UTF-8 && \
    localedef en_US.UTF-8 -i en_US -fUTF-8 && \
    dpkg-reconfigure -f noninteractive locales && \
    echo "LANG=en_US.UTF-8" >> /etc/default/locale && \
    echo "LANGUAGE=en_US.UTF-8" >> /etc/default/locale && \
    echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale

RUN export LANG=en_US.UTF-8 && \
    export LANGUAGE=en_US.UTF-8 && \
    export LC_ALL=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN /usr/sbin/update-locale LANG=en_US.UTF-8
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen

# UTC timezone
RUN echo "UTC" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

ADD get_shibby.sh /bin/
ADD copy_source_to_compile.sh /bin/
RUN useradd -ms /bin/bash tomato && echo 'tomato:shibby-mips' | chpasswd && adduser tomato sudo

