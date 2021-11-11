FROM ubuntu:14.04
MAINTAINER Arcus "http://arcus.io"
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y cron
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y munin
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 libapache2-mod-fcgid libcgi-fast-perl
RUN (grep ScriptAlias /etc/munin/apache.conf > /etc/apache2/sites-available/default-munin.conf)
RUN (sed -e 's/^ScriptAlias/#ScriptAlias/' /etc/munin/apache.conf >> /etc/apache2/sites-available/default-munin.conf)
RUN (sed -i 's/^Alias.*/Alias \/ \/var\/cache\/munin\/www\//g' /etc/apache2/sites-available/default-munin.conf)
RUN (sed -i 's/^\s*Allow from .*/        Allow from all\n        Require all granted/g' /etc/apache2/sites-available/default-munin.conf)
RUN (ln -sf /etc/apache2/sites-available/default-munin.conf /etc/apache2/sites-enabled/000-default.conf)
RUN (mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin)
ADD run.sh /usr/local/bin/run
VOLUME /var/lib/munin
VOLUME /var/log/munin
EXPOSE 80
CMD ["/usr/local/bin/run"]
