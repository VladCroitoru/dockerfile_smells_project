FROM ubuntu:14.04

RUN dpkg --add-architecture i386 && \
    echo "deb http://archive.canonical.com/ $(lsb_release -sc) partner" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y install skype x11-apps

RUN useradd skype -s /bin/bash -m

## Set timezone
#
RUN echo "America/New_York" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

CMD sudo skype -c skype
