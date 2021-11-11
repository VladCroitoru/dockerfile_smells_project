# base - Base Image with supervisord

FROM debian:wheezy

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Base system setup
RUN apt-get -qq update \
    && apt-get -yqq upgrade \
    && apt-get -yqq install apt-utils locales locales-all
ADD locale /etc/default/locale

# Basic packages
RUN apt-get -yqq install vim mc curl wget less python-pip supervisor \
    && pip install supervisor-stdout

ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD sv_stdout.conf /etc/supervisor/conf.d/

CMD ["/usr/bin/supervisord"]
