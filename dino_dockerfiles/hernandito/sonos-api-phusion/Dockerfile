
FROM linuxserver/baseimage


# Set correct environment variables.
ENV DEBIAN_FRONTEND noninteractive
# Set correct environment variables
ENV HOME /root

ADD . /build

RUN mkdir -p /app
RUN mkdir -p /app/settings
RUN mkdir -p /app/presets

ADD . /app

RUN chmod +x /build/prepare.sh
RUN chmod +x /build/install.sh
RUN chmod +x /build/cleanup.sh

RUN bash /build/prepare.sh
RUN	bash /build/install.sh
RUN	bash /build/cleanup.sh

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

EXPOSE 5005
VOLUME /app
ENV TERM=xterm

ADD init/ /etc/my_init.d/
#ADD services/ /etc/service/


RUN chmod +x /etc/my_init.d/10_dbus.sh
