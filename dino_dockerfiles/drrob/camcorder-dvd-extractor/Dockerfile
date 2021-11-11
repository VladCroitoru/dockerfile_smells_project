# Make a base image with updates
FROM phusion/baseimage:0.10.1 as updated
RUN apt-get update && apt-get dist-upgrade -y
CMD ["/sbin/my_init"]

# Build a patched version of subtitleripper
FROM updated as build-subtitleripper
COPY subtitleripper.patch /root/
RUN sed -i 's,# deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse,deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse,' /etc/apt/sources.list \
 && apt-get update \
 && apt-get install build-essential fakeroot -y \
 && apt-get build-dep subtitleripper -y \
 && cd /root \
 && apt-get source subtitleripper -y \
 && cd subtitleripper-[0-9.]* \
 && patch < /root/subtitleripper.patch \
 && dpkg-buildpackage -rfakeroot -uc -b
 
# Build dvd-vr
FROM updated AS build-dvd-vr
ADD https://github.com/pixelb/dvd-vr/archive/927ba99fcf51393b264f36d7edccea211e889939.zip /root/dvd-vr.zip
RUN apt-get install -y unzip build-essential \
 && cd /root \
 && unzip dvd-vr.zip \
 && cd dvd-vr-* \
 && make

# Assemble the dvd-extractor image
FROM updated
COPY --from=build-dvd-vr /root/dvd-vr-*/dvd-vr /usr/local/bin/dvd-vr
COPY --from=build-subtitleripper /root/subtitleripper_*-dmo1ubuntu1_amd64.deb /root/
COPY extract-dvd-video /usr/local/bin/
COPY miniDVD.json /etc/
RUN add-apt-repository ppa:stebbins/handbrake-releases -y \
 && apt-get update \
 && apt-get install transcode handbrake-cli lsdvd -y \
 && apt-get install /root/subtitleripper*.deb -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENTRYPOINT /usr/local/bin/extract-dvd-video
