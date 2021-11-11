FROM ubuntu:bionic

MAINTAINER cmavr8

VOLUME ["/var/lib/backuppc"]

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip debconf-utils msmtp

RUN pip install supervisor

RUN echo "postfix postfix/main_mailer_type select Local only" | debconf-set-selections
RUN echo "postfix postfix/mailname string backuppc.localdomain" | debconf-set-selections
RUN echo "postfix postfix/relayhost string smtp.localdomain" | debconf-set-selections
RUN echo "backuppc backuppc/configuration-note note" | debconf-set-selections
RUN echo "backuppc backuppc/restart-webserver boolean true" | debconf-set-selections
RUN echo "backuppc backuppc/reconfigure-webserver multiselect apache2" | debconf-set-selections

RUN apt-get install -y backuppc apache2-utils

# Add user backuppc to sudoers to be able to access all files without a password
RUN echo "backuppc ALL = NOPASSWD: /bin/tar" >> /etc/sudoers

COPY supervisord.conf /etc/supervisord.conf
COPY msmtprc /var/lib/backuppc/.msmtprc
COPY run.sh /run.sh

RUN sed -i 's/\/usr\/sbin\/sendmail/\/usr\/bin\/msmtp/g' /etc/backuppc/config.pl

RUN chmod 0755 /run.sh

EXPOSE 80

CMD ["/run.sh"]
