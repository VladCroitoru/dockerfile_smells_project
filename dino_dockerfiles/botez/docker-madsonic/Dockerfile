FROM phusion/baseimage:0.9.11
MAINTAINER botez <troyolson1@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN apt-get update -q

# install dependencies for madsonic
RUN apt-get install -qy openjdk-7-jre unzip
RUN apt-get clean

# install madsonic
ADD http://madsonic.org/download/5.1/20140702_madsonic-5.1.4800.beta2.deb /tmp/madsonic.deb
RUN dpkg -i /tmp/madsonic.deb && rm /tmp/madsonic.deb

RUN chown -R nobody:users /var/madsonic

# install update
#ADD http://madsonic.org/download/5.1/20140415_madsonic-5.1.4100.beta1-war-jspc.zip /usr/share/madsonic/update.zip
#RUN cd /usr/share/madsonic && unzip -o update.zip
#RUN chmod +x /usr/share/madsonic/*

EXPOSE 4040
EXPOSE 4050


VOLUME /config
# install latest 64-bit binaries for ffmpeg/lame/etc
ADD http://madsonic.org/download/transcode/20140702_madsonic-transcode_latest_x64.zip /tmp/transcode.zip
RUN unzip /tmp/transcode.zip -d /tmp
RUN cp /tmp/linux/* /var/madsonic/transcode
RUN chown -R nobody:users /var/madsonic/transcode/
RUN chmod -R 777 /var/madsonic/transcode/
#RUN ln -s /var/madsonic/transcode/* /usr/bin/

# Add Madsonic to runit
RUN mkdir /etc/service/madsonic
ADD madsonic.sh /etc/service/madsonic/run
RUN chmod +x /etc/service/madsonic/run

