FROM phusion/baseimage:0.9.16
MAINTAINER Shane Starcher

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get -y install ruby ruby-dev build-essential libcurl3 libcurl3-gnutls libcurl4-openssl-dev
RUN gem install json --no-ri --no-rdoc
RUN gem install fog --no-ri --no-rdoc

ADD . /opt/vacuumetrix
ADD ./conf/cron.conf /etc/cron.d/vacuumetrix
RUN crontab /etc/cron.d/vacuumetrix


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
