# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:latest

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
RUN apt-get update && apt-get dist-upgrade -y && mkdir -p /etc/my_init.d
COPY fhem.sh /etc/my_init.d/fhem.sh
RUN chmod +x /etc/my_init.d/fhem.sh
RUN apt-get update
RUN apt-get -y install perl-base libdevice-serialport-perl libwww-perl libio-socket-ssl-perl \
libcgi-pm-perl libjson-perl sqlite3 libdbd-sqlite3-perl libtext-diff-perl libtimedate-perl \
libmail-imapclient-perl libgd-graph-perl libtext-csv-perl libxml-simple-perl liblist-moreutils-perl \
ttf-liberation libimage-librsvg-perl libgd-text-perl libsocket6-perl libio-socket-inet6-perl \
libmime-base64-perl libimage-info-perl libusb-1.0-0-dev libnet-server-perl usbutils build-essential wget
#RUN echo | cpan -i inc::latest
RUN echo | cpan -i Module::Pluggable


EXPOSE 8083

VOLUME /opt/fhem/

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
