FROM ubuntu:trusty
MAINTAINER Pavel Bezrukov "bezrukov.ps@gmail.com"

# Get noninteractive frontend for Debian to avoid some problems:
#    debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

COPY etc/apt/sources.list.d/additional.list /etc/apt/sources.list.d/

# Install packages
RUN apt-get update
RUN apt-get dist-upgrade -y && apt-get upgrade -y && apt-get autoremove -y && sudo apt-get autoclean -y

# Install base programm
RUN apt-get -y -q install mc vim nano iputils-ping telnet htop wget man sudo curl cron \
  tar unzip git logrotate tzdata pwgen \
  openssl openssl-blacklist ssl-cert

# Install russian lang
RUN apt-get -y -q install language-pack-ru
RUN update-locale LANG=ru_RU.UTF-8
RUN locale -a
COPY etc/default/locale /etc/default/

# Moscow timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone

# Add user
RUN useradd -G sudo -s /bin/bash -Um bezr

EXPOSE 22

# Define default command.
CMD ["/bin/bash", "-l"]

