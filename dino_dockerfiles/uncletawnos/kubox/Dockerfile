FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /etc/apt/conf.d \
    && echo 'APT::Install-Recommends "false";' > /etc/apt/conf.d/recommends.conf \
    && echo 'APT::Install-Suggests "false";' >> /etc/apt/conf.d/recommends.conf

#Fix debian slim missing man dirs errors
RUN seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{}
RUN apt-get update \
    && apt-get -y install apt-utils \
    && apt-get -y dist-upgrade \
    && apt-get -y auto-remove \
    && apt-get -y install \
       wget dnsutils netcat curl telnet iputils-ping links \
       gnupg net-tools inetutils-traceroute \
       git vim-nox gettext-base bash-completion jq patch gawk \
       default-mysql-client postgresql-client redis-tools kafkacat \
    && apt-get clean


RUN mkdir -p /etc/bash.bashrc.d \
    && wget https://raw.githubusercontent.com/UncleTawnos/bashmash/master/system_aliases -O /etc/bash.bashrc.d/system_aliases \
    && wget https://raw.githubusercontent.com/UncleTawnos/bashmash/master/bash_time_history -O /etc/bash.bashrc.d/bash_time_history \
    && wget https://raw.githubusercontent.com/UncleTawnos/bashmash/master/vimrc.local -O /etc/vim/vimrc.local \
    && wget https://raw.githubusercontent.com/UncleTawnos/bashmash/master/bashrc.patch -O /tmp/bashrc.patch \
    && patch --dry-run /etc/bash.bashrc < /tmp/bashrc.patch \
    && patch /etc/bash.bashrc < /tmp/bashrc.patch


CMD ["/bin/bash"]
