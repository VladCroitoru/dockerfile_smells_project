# base image is stratolinux/baseimage-docker
FROM stratolinux/baseimage-docker:0.9.19
MAINTAINER Eric Young <eric@stratolinux.com>
ENV APPDIR /opt/headphones

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# To get rid of error messages like "debconf: unable to initialize frontend: Dialog":
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >> /etc/apt/sources.list
RUN apt-get -qy update && apt-get -qy upgrade


# shared volumes
VOLUME /config
VOLUME /music
VOLUME /downloads
# ports
EXPOSE 8181

# ...put your own build instructions here...
RUN apt-get install -qy git python unrar python-software-properties software-properties-common wget

# now install sickrage
RUN git clone https://github.com/rembo10/headphones.git $APPDIR

COPY etc/ /etc/

RUN chmod +x /etc/my_init.d/*
RUN find /etc/service -name run -exec chmod +x {} \;

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
