FROM ubuntu:16.04

MAINTAINER joshhsoj1902

RUN apt-get update \
 && apt-get install -y  subversion \
                        build-essential \
                        libxml-parser-perl \
                        libarchive-extract-perl \
                        libarchive-zip-perl \
                        libpath-class-perl \
                        wget \
                        curl \
                        unzip \
                        lib32gcc1 \
                        lib32stdc++6 \
                        perl-modules \
                        pure-ftpd \
                        e2fsprogs \
                        libhttp-daemon-perl \
                        libarchive-any-perl \
                        default-jre \
                        git

COPY rsync /root/rsync

VOLUME ["games:/srv/games/"]

WORKDIR /root/rsync

CMD ["perl", "RunUpdate.pl", "update", "all"]
