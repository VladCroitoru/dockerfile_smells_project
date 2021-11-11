FROM phusion/baseimage:0.9.16
MAINTAINER David Young <davidy@funkypenguin.co.nz>
#Based on the work of needo <needo@superhero.org>
#ENV DEBIAN_FRONTEND noninteractive

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/sabnzbd.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Add a generic htpc user, which we'll reuse for all HTPC containers, and set UID predictable value (the meaning of 2 lives)
RUN useradd htpc -u 4242

RUN add-apt-repository ppa:jcfp/ppa
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
RUN add-apt-repository ppa:fnu/main-fnu
RUN apt-get update -q
RUN apt-get install -qy unrar par2 sabnzbdplus wget ffmpeg sabnzbdplus-theme-mobile

# Path to a directory that only contains the sabnzbd.conf
VOLUME /config
VOLUME /downloads

EXPOSE 8080 9090

# Add sabnzbd to runit
RUN mkdir /etc/service/sabnzbd
ADD sabnzbd.sh /etc/service/sabnzbd/run
RUN chmod +x /etc/service/sabnzbd/run
