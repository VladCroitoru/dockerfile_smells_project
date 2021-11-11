FROM ubuntu:16.04
MAINTAINER technojunkie

ENV VERSION 1.10.8

WORKDIR /tmp
ADD http://www.makemkv.com/download/makemkv-bin-$VERSION.tar.gz makemkv-bin-$VERSION.tar.gz
ADD http://www.makemkv.com/download/makemkv-oss-$VERSION.tar.gz makemkv-oss-$VERSION.tar.gz
ADD start.sh /usr/local/bin

RUN apt-get -y update && apt-get install -y \
    build-essential \
    handbrake-cli \
    less \
    libavcodec-dev \
    libc6-dev \
    libdvdnav4 \
    libdvdread4 \
    libexpat1-dev \
    libssl-dev \
    libudev-dev \
    openssh-server \
    perl \
    pkg-config \
    screen \
    software-properties-common; \
    tar xzf makemkv-oss-$VERSION.tar.gz; \
    cd makemkv-oss-$VERSION; \
    ./configure --disable-gui; \
    make; \
    make install; \
    cd ..; \
    tar xzf makemkv-bin-$VERSION.tar.gz; \
    cd makemkv-bin-$VERSION; \
    mkdir tmp; \
    echo "accepted" > tmp/eula_accepted; \
    make install; \
    cd ..; \
    rm -rf makemkv-*; \
    apt-get -y remove build-essential && apt-get -y autoremove

ENV NOTVISIBLE "in users profile"
RUN mkdir /var/run/sshd; \
    echo 'root:screencast' | chpasswd; \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config; \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd; \
    echo "export VISIBLE=now" >> /etc/profile; \
    chmod +x /usr/local/bin/start.sh

RUN groupadd -r ripbot && useradd -r -g ripbot ripbot


EXPOSE 22
VOLUME ["/work"]
CMD ["start.sh"]
