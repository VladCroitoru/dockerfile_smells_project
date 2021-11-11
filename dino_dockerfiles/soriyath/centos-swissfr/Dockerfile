FROM centos:centos7
MAINTAINER Sumi Straessle

RUN yum upgrade -y \
	&& yum install -y yum groupinstall "Development Tools" \
	&& yum install -y git less vim curl wget unzip ncurses ncurses-devel gcc make \
	&& yum -y -q reinstall glibc-common systemd

RUN echo "fr_CH.UTF-8 UTF-8">/etc/locale.conf \
	&& rm /etc/localtime \
	&& ln -s /usr/share/zoneinfo/Europe/Zurich /etc/localtime

# Set environment variables for locale
ENV LANG fr_CH.UTF-8  
ENV LANGUAGE fr_CH:fr
ENV LC_ALL fr_CH.UTF-8 

WORKDIR /usr/local/src
RUN wget http://hisham.hm/htop/releases/2.0.2/htop-2.0.2.tar.gz \
	&& tar xzf htop-2.0.2.tar.gz \
	&& rm -f htop-2.0.2.tar.gz \
	&& cd htop-2.0.2 \
	&& ./configure \
	&& make -j $(cat /proc/cpuinfo | grep processor | wc -l) \
	&& make install \
	&& cd .. \
	&& rm -rf htop-2.0.2

# Install and configure Supervisor
RUN yum install -y python-setuptools \
	&& easy_install pip \ 
	&& pip install supervisor \
	&& mkdir -p /etc/supervisor/conf.d
ADD supervisor.conf /etc/supervisor/supervisor.conf

# Clean container
RUN yum -y clean all \
	&& yum -y autoremove \
	&& rm -rf ~/.cache/pip/*

# default command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
