FROM centos:7
MAINTAINER Robin Dietrich <me@invokr.org>
MAINTAINER Christoph Wurst <christoph@winzerhof-wurst.at>

# Install postfix, dovecot, and supervisor
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
 && yum update -y && yum upgrade -y && yum install -y cronie cyrus-sasl dovecot opendkim \
    opendmarc postfix python-setuptools pypolicyd-spf rsyslog wget && easy_install pip \
 && pip install supervisor mako && yum clean all

# For debugging
# RUN yum install -y telnet vim mailx

# Environment variables
ENV POSTFIX_HOSTNAME="mail.domain.tld"

# Add scripts and config
ADD scripts /opt/bin
ADD config /opt/config

# Add group and user for virtual mail
RUN groupadd -g 10000 vmail && useradd -m -d /vmail -u 10000 -g 10000 -s /sbin/nologin vmail && chmod 755 /vmail \
 && usermod -G vmail postfix && usermod -G vmail dovecot

# Add secure directory
RUN mkdir -p /secure/postfix && touch /secure/postfix/vmaps /secure/postfix/vhosts /secure/postfix/vuids /secure/postfix/vgids \
 && mkdir -p /secure/dovecot && touch /secure/dovecot/users /secure/dovecot/passwd

# Configure supervisord
ADD config/supervisor/supervisord.conf /etc/supervisord.conf

# Configure rsyslogd
ADD config/rsyslog/file.conf /etc/rsyslog.conf

# Configure opendmarc
ADD config/opendmarc/opendmarc.conf /etc/opendmarc.conf
RUN ln -s /opt/bin/update-tld-names /etc/cron.weekly/ && /opt/bin/update-tld-names

# Configure postfix
ADD config/postfix /etc/postfix/

# Configure dovecot
ADD config/dovecot /etc/dovecot

# Expose smtpd, submission and imaps
EXPOSE 25
EXPOSE 587
EXPOSE 993

# Start our init system
CMD ["/opt/bin/dumb-init", "/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
