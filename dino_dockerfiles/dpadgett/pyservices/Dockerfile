# Dockerfile to run the JKA demo site python services
FROM ubuntu:18.04
MAINTAINER Dan Padgett <dumbledore3@gmail.com>

RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections; \
    apt-get update -qqy \
 && apt-get install -qqy --no-install-recommends \
        tzdata \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    locales \
    python \
    python-falcon \
    python-dateutil \
    python-tz \
    python-mpmath \
    python-pip \
    python-sklearn \
    python-sklearn-lib \
    libjansson4 \
    apache2 \
    nano \
    ssh \
    zip && \
  pip install trueskill pymongo && \
  apt-get remove --purge --auto-remove -y python-pip && apt-get clean && apt-get autoclean

RUN cp /usr/share/i18n/charmaps/CP1252.gz /tmp && \
    cd /tmp && \
    gzip -d CP1252.gz && \
    localedef -f /tmp/CP1252 -i /usr/share/i18n/locales/en_US  /usr/lib/locale/en_US.CP1252

RUN cp /usr/share/i18n/charmaps/UTF-8.gz /tmp && \
    cd /tmp && \
    gzip -d UTF-8.gz && \
    localedef -f /tmp/UTF-8 -i /usr/share/i18n/locales/en_US  /usr/lib/locale/en_US.UTF-8

RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

RUN sed -i 's/Listen 80/Listen 3031/' /etc/apache2/ports.conf
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod cgid
RUN a2enmod rewrite

RUN useradd -ms /bin/bash pyservices

# copy the nice dotfiles that dockerfile/ubuntu gives us:
RUN cd && cp -R .bashrc .profile /home/pyservices

COPY python/* /home/pyservices/

WORKDIR /home/pyservices

RUN chown -R pyservices:pyservices /home/pyservices

ENV HOME /home/pyservices
ENV USER pyservices

ENV APACHE_RUN_USER pyservices
ENV APACHE_RUN_GROUP pyservices
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

CMD /usr/sbin/apache2ctl -D FOREGROUND
