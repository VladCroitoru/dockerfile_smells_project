FROM ubuntu:trusty

MAINTAINER me@endikaiglesias.com

RUN locale-gen en_US.UTF-8 && update-locale && echo 'LANG="en_US.UTF-8"' > /etc/default/locale
RUN apt-get install -y aptitude git && aptitude update && aptitude dist-upgrade -y
