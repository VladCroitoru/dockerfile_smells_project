FROM phusion/baseimage:0.9.16
MAINTAINER needo <needo@superhero.org>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody && \
usermod -g 100 nobody && \

add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse" && \
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse" && \
apt-get update -q && \

# Install Dependencies
apt-get install -qy python python-cheetah ca-certificates wget unrar unzip && \

# Install SickRage 0.2.1 (2014-10-22)
mkdir /opt/sickrage && \
cd /tmp && \
wget https://github.com/SiCKRAGETV/SickRage/archive/v4.0.9.zip && \
unzip v4.0.9.zip && \
mv SickRage-4.0.9/* /opt/sickrage/ && \
chown -R nobody:users /opt/sickrage && \

# clean up
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
/usr/share/man /usr/share/groff /usr/share/info \
/usr/share/lintian /usr/share/linda /var/cache/man && \
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
(( find /usr/share/doc -empty|xargs rmdir || true ))

EXPOSE 8081

# SickRage Configuration
VOLUME /config

# Downloads directory
VOLUME /downloads

# TV directory
VOLUME /tv

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add SickRage to runit
RUN mkdir /etc/service/sickrage
ADD sickrage.sh /etc/service/sickrage/run
RUN chmod +x /etc/service/sickrage/run
