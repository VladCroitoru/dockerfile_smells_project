FROM ubuntu:latest

MAINTAINER XtremXpert <xtremxpert@xtremxpert.com>

ENV LC_ALL fr_CA.UTF-8
ENV OS UBUNTU14_64

ENV ZIMBRA zcs-8.6.0_GA_1153.UBUNTU14_64.20141215151116

RUN apt-get -y update && \
	apt-get -y install \
		curl \
		sudo \
		tar \
		wget \
		tar \
		perl \
		sysstat \
		hostname \
		libidn11 \
		libpcre3 \
		libexpat1 \
		libgmp3-dev \
		patch \
		pax \
		sqlite3 \
		libaio1 \
		unzip  \
		netcat-openbsd \
		inetutils-ping \
		net-tools \
		openssh-server \
		libperl5.18 \
	&& \
	mkdir /tmp/zcs && \ 
	cd /tmp/zcs && \
	wget http://files2.zimbra.com/downloads/8.6.0_GA/$ZIMBRA.tgz && \
	tar xzvf $ZIMBRA.tgz && \
	mv $ZIMBRA zcs-install && \
	mkdir /var/run/sshd && \
	locale-gen --no-purge fr_CA.UTF-8 && \
	update-locale LANG=fr_CA.UTF-8

ADD config.defaults /tmp/zcs/config.defaults
ADD utilfunc8.0.8.sh /tmp/zcs/utilfunc.sh
ADD start.sh /start.sh

RUN cp /tmp/zcs/utilfunc.sh /tmp/zcs/zcs-install/util/utilfunc.sh && \
	echo 'root:zimbra' |chpasswd && \
	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
	cd /tmp/zcs/zcs-install && \
	./install.sh -s --platform-override /tmp/zcs/config.defaults && \
	mv /opt/zimbra /opt/installzimbra && \
	chmod +x /start.sh

VOLUME ["/home"]
VOLUME ["/opt/zimbra"]

EXPOSE 22
EXPOSE 389
EXPOSE 25
EXPOSE 456
EXPOSE 587
EXPOSE 110
EXPOSE 143
EXPOSE 993
EXPOSE 995
EXPOSE 80
EXPOSE 443
EXPOSE 8080
EXPOSE 8443
EXPOSE 7071

CMD ["/start.sh"]
