FROM centos:centos7

MAINTAINER Wilco Eliveld <wilcoeliveld@gmail.com>

RUN yum -y install \
	git \
	python-cheetah \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

RUN mkdir /opt/auto-sub
RUN git clone https://github.com/BenjV/autosub.git /opt/auto-sub

ADD config/config.properties /opt/auto-sub/

RUN rm -rf /etc/ld.so.cache \ 
	; rm -rf /sbin/sln \
	; rm -rf /usr/{{lib,share}/locale,share/{man,doc,info,gnome/help,cracklib,il8n},{lib,lib64}/gconv,bin/localedef,sbin/build-locale-archive} \
	; rm -rf /var/cache/{ldconfig,yum}/*

EXPOSE 8083

VOLUME /tv

WORKDIR /opt/auto-sub
CMD python AutoSub.py
