FROM debian:stretch
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive

# NB ntp is set in base VM (host on linux hosts, most likely boot2docker on Windows and Mac)
# Time of the containers is the time of the host machine

# --no-install-recommends by default and disable doc and manpage
COPY 01norecommend $ROOTFS/etc/apt/apt.conf.d/01norecommend
COPY 01_nodoc $ROOTFS/etc/dpkg/dpkg.conf.d/01_nodoc

# Set the locale (Debian removed dependency to locale in 2011)
RUN apt-get update \
	&& apt-get install -y locales curl git htop man software-properties-common unzip vim wget apt-transport-https \
	&& echo "fr_CH.UTF-8 UTF-8" > /etc/locale.gen \
	&& locale-gen fr_CH.UTF-8 \
	&& update-locale LANG=fr_CH.UTF-8 \
	&& cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime \
	&& echo "Europe/Zurich" > /etc/timezone \
	&& dpkg-reconfigure -f noninteractive tzdata \
	&& printf 'LANG=fr_CH.utf8\nLANGUAGE=fr_CH:fr\nLC_CTYPE="fr_CH.utf8"\nLC_ALL=fr_CH.utf8'>/etc/default/locale

# Set environment variables for locale
ENV LANG fr_CH.UTF-8  
ENV LANGUAGE fr_CH:fr
ENV LC_ALL fr_CH.UTF-8 

# supervisor installation, create directory for child images to store configuration in
RUN apt-get -y install supervisor && \
  mkdir -p /var/log/supervisor && \
  mkdir -p /etc/supervisor/conf.d
COPY supervisor.conf /etc/supervisor/supervisor.conf

# Debian unattended upgrades, comment to deactivate
RUN apt-get install -y unattended-upgrades apt-listchanges
COPY 50unattended-upgrades $ROOTFS/etc/apt/apt.conf.d/50unattended-upgrades
COPY 02periodic $ROOTFS/etc/apt/apt.conf.d/02periodic

RUN apt-get -y upgrade \
	&& apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# default command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
