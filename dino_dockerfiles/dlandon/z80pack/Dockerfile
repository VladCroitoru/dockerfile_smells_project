FROM phusion/baseimage:bionic-1.0.0 as builder

LABEL maintainer="dlandon"

FROM builder as build1
ENV	DEBCONF_NONINTERACTIVE_SEEN="true" \
	DEBIAN_FRONTEND="noninteractive" \
	DISABLE_SSH="true" \
	HOME="/root" \
	LC_ALL="C.UTF-8" \
	LANG="en_US.UTF-8" \
	LANGUAGE="en_US.UTF-8" \
	TZ="Etc/UTC" \
	TERM="xterm" \
	Z80PACK_VERS="1.37" \
	CPMTOOLS_VERS="2.22"

FROM build1 as build2
COPY init /etc/my_init.d/

FROM build2 as build3
RUN	rm -rf /etc/service/cron /etc/service/syslog-ng

FROM build3 as build4
RUN	apt-get update && \
	apt-get -y dist-upgrade -o Dpkg::Options::="--force-confold" && \
	apt-get -y upgrade -o Dpkg::Options::="--force-confold" && \
	apt-get -y install wget tzdata make gcc nano sudo && \
	apt-get -y install libncurses5-dev libncursesw5-dev && \
	wget http://archive.ubuntu.com/ubuntu/pool/universe/s/shellinabox/shellinabox_2.14-1_amd64.deb && \
	dpkg -i shellinabox_2.14-1_amd64.deb

FROM build4 as build5
RUN	cd ~ && \
	wget http://www.autometer.de/unix4fun/z80pack/ftp/z80pack-$Z80PACK_VERS.tgz && \
	tar xzvf z80pack-$Z80PACK_VERS.tgz && \
	mv z80pack-$Z80PACK_VERS z80pack	&& \
	rm z80pack-$Z80PACK_VERS.tgz

FROM build5 as build6
RUN	cd ~/z80pack/cpmsim/srcsim && \
	make -fMakefile.linux && \
	make -fMakefile.linux clean

FROM build6 as build7
RUN	cd ~/z80pack/cpmsim/srctools && \
	sed -i "s/"#INSTALLDIR="/"INSTALLDIR=/"" Makefile && \
	make && \
	make install && \
	make clean

FROM build7 as build8
RUN	cd ~ && \
	wget http://www.moria.de/~michael/cpmtools/files/cpmtools-$CPMTOOLS_VERS.tar.gz && \
	tar xzvf cpmtools-$CPMTOOLS_VERS.tar.gz && \
	mv cpmtools-$CPMTOOLS_VERS cpmtools && \
	cd cpmtools && \
	./configure && make && make install && \
	cd ~ && \
	rm cpmtools-$CPMTOOLS_VERS.tar.gz && \
	rm -r cpmtools

FROM build8 as build9
RUN	cd ~/z80pack/cpmsim/disks/library && \
	mkdir -p ../backups && \
	cp -p * ../backups

FROM build9 as build10
RUN	sed -i s#SHELL=/bin/sh#SHELL=/bin/bash#g /etc/default/useradd && \
	useradd -d "/root/z80pack/cpmsim" "vintage" && \
	adduser "vintage" sudo && \
	echo "vintage:computer" | chpasswd

FROM build10 as build11
RUN	mv "/etc/shellinabox/options-enabled/00+Black on White.css" "/etc/shellinabox/options-enabled/00_Black on White.css" && \
	mv "/etc/shellinabox/options-enabled/00_White On Black.css" "/etc/shellinabox/options-enabled/00+White On Black.css"

FROM build11 as build12
RUN	apt-get -y remove wget make gcc libncurses5-dev libncursesw5-dev && \
	apt-mark hold shellinabox && \
	apt-get clean -y && \
	apt-get -y autoremove && \
	rm -rf /tmp/* /var/tmp/* && \
	chmod +x /etc/my_init.d/*.sh

FROM build12 as build13
VOLUME ["/config"]

FROM build13 as build14
EXPOSE 4200

FROM build14
CMD ["/sbin/my_init"]
