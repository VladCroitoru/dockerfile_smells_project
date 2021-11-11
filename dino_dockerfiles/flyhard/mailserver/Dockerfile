FROM flyhard/debian-consul
MAINTAINER Per Abich <per.abich@gmail.com>

ADD scripts/ /scripts
RUN /scripts/install.sh
RUN /scripts/postgres-setup.sh

# Add a local user to receive mail at someone@example.com, with a delivery directory
# (for the Mailbox format).
#RUN useradd -s /bin/bash someone
#RUN mkdir /var/spool/mail/someone
#RUN chown someone:mail /var/spool/mail/someone

RUN chown root:root /etc/aliases
RUN newaliases
ADD /config/rsyslog-logrotate.conf /etc/logrotate.d/rsyslog
ADD /config/access_sender /etc/postfix/access_sender
ADD /config/rsyslog.conf /etc/rsyslog.conf
RUN postmap /etc/postfix/access_sender
# Use syslog-ng to get Postfix logs (rsyslog uses upstart which does not seem
# to run within Docker).
#RUN apt-get install -q -y syslog-ng

EXPOSE 25
RUN chmod +x /scripts/entrypoint.sh /scripts/run.sh

RUN /scripts/getConfdLatest.sh
# Debug stuff
RUN apt-get update
RUN apt-get install -y swaks less

ADD confd /etc/confd
ADD consul /etc/consul/

RUN /usr/sbin/logrotate -f /etc/logrotate.conf

ENTRYPOINT ["/scripts/entrypoint.sh"]
CMD ["/scripts/run.sh"]

