FROM ubuntu
MAINTAINER Tomas Maggio <info@sensaway.co.nz>

ENV DEBCONF_NONINTERACTIVE_SEEN=true
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Pacific/Auckland
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
      apt-get -y install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN apt-get update
RUN apt-get install -y software-properties-common wget
RUN add-apt-repository -y ppa:iconnor/zoneminder
RUN apt-get update
RUN apt-get install -y mariadb-server \
    mariadb-client \
    nginx \
    nginx-extras \
    fcgiwrap \
    php7.0-fpm \
    ntp \
    htop \
    wget \
    php7.0 \
    php7.0-mysql \
    php7.0-curl \
    php7.0-gd \
    php7.0-intl \
    php-pear \
    php-imagick \
    php7.0-imap \
    php7.0-mcrypt \
    php-memcache \
    php7.0-pspell \
    php7.0-recode \
    php7.0-sqlite3 \
    php7.0-tidy \
    php7.0-xmlrpc \
    php7.0-xsl \
    php7.0-mbstring \
    php-gettext \
    php-apcu \
    php-gd \
    vim \
    usbutils
RUN apt-get clean

RUN adduser www-data video
COPY backend.conf /etc/nginx/conf.d/backend.conf

#Comment out if using Apache2
#RUN a2enconf zoneminder
#RUN a2enmod cgi
#RUN a2enmod rewrite

COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 777 /docker-entrypoint.sh
RUN adduser www-data video
USER docker
RUN export XDG_RUNTIME_DIR=/run/user/`id -u`
CMD ["/docker-entrypoint.sh"]
#ENTRYPOINT ["/docker-entrypoint.sh"]
RUN echo "Open Zoneminder in a web browser (http://server-ip/zm). Click on Options - Paths and change PATH_ZMS to /zm/cgi-bin/nph-zms Click the Save button. Press enter to continue"
RUN echo "If you plan to use the API go to https://wiki.zoneminder.com/Ubuntu_Server_16.04_64-bit_with_Zoneminder_1.30.0_the_easy_way and follow the instructions for the API fix. Press Enter to finish."
EXPOSE 80
