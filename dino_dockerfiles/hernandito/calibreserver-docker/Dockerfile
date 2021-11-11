
FROM phusion/baseimage:0.9.15

MAINTAINER hernando

# Set correct environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TERM xterm


# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN apt-get update
RUN apt-get install -qy mc

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
wget \
python \
xdg-utils \
ImageMagick && \
mkdir /opt/calibre

RUN mkdir /downloads
RUN mkdir /config

VOLUME ["/config", "/opt/calibre", "/downloads" ]

EXPOSE 8080


# Add firstrun.sh to execute during container startup
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

# Add our crontab file
#ADD crons.conf /root/crons.conf
ADD crons.conf /home/crons.conf


# Use the crontab file
#RUN crontab  /opt/calibre/crons.conf

# Start cron
#RUN cron

# The commands below are now run in firstrun.sh. Not needed here anymore.
#RUN cd /opt && \
#wget --no-check-certificate -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main('/opt/', True)"
#CMD ["/opt/calibre/calibre-server","--with-library=/config"]

