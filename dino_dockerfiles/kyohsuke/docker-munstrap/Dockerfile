FROM ubuntu:14.04
MAINTAINER Keisuke Kawahara <kyohsuke@conafie.jp>

# Install
RUN apt-get update &&\
    apt-get -y upgrade &&\
    RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y git-core wget cron munin apache2 libapache2-mod-fcgid libcgi-fast-perl &&\
    apt-get -qq -y clean &&\
    apt-get -qq -y autoclean &&\
    apt-get -qq -y autoremove

# Configure
RUN (grep ScriptAlias /etc/munin/apache.conf > /etc/apache2/sites-available/default-munin.conf) &&\
    (sed -e 's/^ScriptAlias/#ScriptAlias/' /etc/munin/apache.conf >> /etc/apache2/sites-available/default-munin.conf) &&\
    (sed -i 's/^Alias.*/Alias \/ \/var\/cache\/munin\/www\//g' /etc/apache2/sites-available/default-munin.conf) &&\
    (sed -i 's/^\s*Allow from .*/        Allow from all\n        Require all granted/g' /etc/apache2/sites-available/default-munin.conf) &&\
    (ln -sf /etc/apache2/sites-available/default-munin.conf /etc/apache2/sites-enabled/000-default.conf) &&\
    (mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin) &&\
    (sed -i -e 's/\[localhost.localdomain\]/\[munin.docker\]/g' /etc/munin/munin.conf)

# munstrap
RUN cd /etc/munin &&\
    git clone https://github.com/jonnymccullagh/munstrap.git &&\
    cp -rb munstrap/templates . &&\
    cp -rb munstrap/static . &&\
    rm -rf ./munstrap

# adding spawn-fcgi
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y spawn-fcgi &&\
    apt-get -qq -y clean &&\
    apt-get -qq -y autoclean &&\
    apt-get -qq -y autoremove

# Finalize
ADD run.sh /usr/local/bin/run
VOLUME /var/lib/munin
VOLUME /var/log/munin
EXPOSE 80
CMD ["/usr/local/bin/run"]
