FROM debian:jessie
MAINTAINER yaasita

# dev
#ADD 02proxy /etc/apt/apt.conf.d/02proxy
#ADD authorized_keys /root/.ssh/authorized_keys

#apt
RUN apt-get update
RUN apt-get upgrade -y

#package
RUN apt-get install -y \
 apache2 \
 aptitude \
 git \
 htop \
 libapache2-mod-php5 \
 openssh-server \
 php5 \
 squirrelmail \
 squirrelmail-locales \
 supervisor \
 vim \
 w3m

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install postfix dovecot-imapd

# ssh
RUN mkdir /var/run/sshd/ && \
 perl -i -ple 's/^(permitrootlogin\s)(.*)/\1yes/i' /etc/ssh/sshd_config && \
 echo root:root | chpasswd

# squirrelmail
ADD etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD etc/squirrelmail/apache.conf /etc/squirrelmail/apache.conf

# supervisor
ADD etc/supervisor/conf.d/blackhole.conf /etc/supervisor/conf.d/blackhole.conf

# mail
RUN useradd mailuser -m && echo mailuser:mailuser | chpasswd
ADD etc/postfix/main.cf /etc/postfix/main.cf
ADD etc/postfix/domains /etc/postfix/
ADD etc/postfix/aliases.reg /etc/postfix/
ADD etc/dovecot/conf.d/10-mail.conf /etc/dovecot/conf.d/10-mail.conf
ADD etc/squirrelmail/config.php /etc/squirrelmail/config.php

EXPOSE 22 25 80
CMD ["/usr/bin/supervisord"]
