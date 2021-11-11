FROM ubuntu:bionic

MAINTAINER Sean H <sahsu.mobi@gmail.com>

RUN adduser --system --home /var/lib/munin --shell /bin/false --uid 1103 --group munin

RUN apt-get update -qq && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \
    apt-get install -y -qq cron munin munin-node nginx wget spawn-fcgi libcgi-fast-perl telnet mtr wget dnsutils sysstat net-tools lsof vim rrdcached rsyslog ssh munin-async htop
RUN rm /etc/nginx/sites-enabled/default && mkdir -p /var/cache/munin/www && chown munin:munin /var/cache/munin/www && mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin

VOLUME /var/lib/munin
VOLUME /var/log/munin

ADD ./munin.conf /etc/munin/munin.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./nginx-munin /etc/nginx/sites-enabled/munin
ADD ./start-munin.sh /munin
ADD ./plugins /plugins/

#EXPOSE 8080
CMD ["bash", "/munin"]
