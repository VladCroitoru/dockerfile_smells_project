FROM cloudposse/apache

MAINTAINER  Erik Osterman "e@osterman.com"

ENV APACHE_EVENT_START_SERVERS             2
ENV APACHE_EVENT_MIN_SPARE_THREADS         25
ENV APACHE_EVENT_MAX_SPARE_THREADS         75
ENV APACHE_EVENT_THREAD_LIMIT              64
ENV APACHE_EVENT_THREADS_PER_CHILD         25
ENV APACHE_EVENT_MAX_REQUEST_WORKERS       150
ENV APACHE_EVENT_MAX_CONNECTIONS_PER_CHILD 0

ENV PERL_MM_USE_DEFAULT true

USER root

# Update the package repository
RUN apt-get update && \
    apt-get install -y software-properties-common  && \
    apt-add-repository multiverse && \
    apt-get update && \
    apt-get install -y apache2-mpm-event libapache2-mod-fcgid libtest-requires-perl libtest-exception-perl libdbd-mysql-perl libdbd-mysql libcgi-session-perl libcgi-fast-perl libfcgi-perl libmath-random-perl libjson-perl && \
    a2dismod mpm_prefork && \
    a2dismod mpm_worker && \
    a2enmod mpm_event && \
    a2enmod fcgid && \
    apt-get clean && \
    cpan install Algorithm::BinPack::2D

ADD conf-available/ /etc/apache2/conf-available/
ADD mods-available/ /etc/apache2/mods-available/
ADD start /start


