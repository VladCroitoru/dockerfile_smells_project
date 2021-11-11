FROM debian:9-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y wget lsb-release gnupg libterm-readline-gnu-perl && \
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.9-1_all.deb -O /root/mysql-apt.config.deb && \
    dpkg -i /root/mysql-apt.config.deb && \
    mkdir -p /usr/share/man/man1/ && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        sudo \
        ca-certificates \
        build-essential \
        uuid-dev \
        libgmp3-dev \
        libxml2-dev \
        libexpat1-dev \
        zlib1g-dev \
        libssl-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libgif-dev \
        libv8-dev \
        libmysqlclient-dev \
        libssh2-1-dev \
        openjdk-8-jre-headless && \
        rm -rf /usr/local/share/man/* /root/*.deb && \
        apt-get clean -y

COPY ./cpanfile /root
RUN wget -O- http://git.io/cpm | perl - install --global --cpanfile=/root/cpanfile && \
        rm -rf /root/.perl-cpm/* /root/.cpanm/* && \
        apt-get remove build-essential -y && \
        apt-get autoremove -y


RUN useradd -ms /bin/bash k1plaza && echo 'k1plaza ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/k1plaza
WORKDIR /k1plaza
RUN mkdir /projects file_storage repositories managed_apps && \
    chown k1plaza:k1plaza /projects file_storage repositories managed_apps



ADD ./script script
ADD ./share/backend share/backend
ADD ./share/system share/system
ADD ./share/backoffice share/backoffice
ADD ./share/developer share/developer
ADD ./lib lib

USER k1plaza:k1plaza
EXPOSE 3000
STOPSIGNAL SIGTERM
ENV MOJO_MODE=development K1PLAZA_DEVELOPER=1
ENTRYPOINT ["./script/k1plaza", "daemon"]
