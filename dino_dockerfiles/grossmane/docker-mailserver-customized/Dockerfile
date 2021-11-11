FROM tvial/docker-mailserver:2.1
MAINTAINER Jens Grossmann <grossmane@users.noreply.github.com>

#ENV http_proxy http://proxy:8080
#ENV https_proxy http://proxy:8080

RUN apt-get -qq update
RUN apt-get install -qq dovecot-mysql postfix-mysql vim

RUN sed -i -e '/\!include auth-sql\.conf\.ext/s/^#//' /etc/dovecot/conf.d/10-auth.conf

RUN sed -i 's/^ignoreip = 127.0.0.1\/8/ignoreip = 127.0.0.1\/8 radicale roundcube cloud/' /etc/fail2ban/jail.conf

COPY dovecot/conf.d/auth-sql.conf.ext /etc/dovecot/conf.d/
COPY dovecot/dovecot-sql.conf.ext /etc/dovecot/dovecot-sql.conf.ext

RUN postconf -e "virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-mailbox-domains.cf"
RUN postconf -e "virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-maps.cf,mysql:/etc/postfix/mysql-virtual-verteiler-alias-maps.cf,mysql:/etc/postfix/mysql-virtual-system-alias-maps.cf,mysql:/etc/postfix/mysql-email2email.cf,mysql:/etc/postfix/mysql-virtual-lists-alias-maps.cf"
RUN postconf -e "virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-maps.cf"

RUN postconf -e "smtpd_recipient_restrictions = permit_sasl_authenticated, permit_mynetworks, reject_unauth_destination, reject_unauth_pipelining, reject_invalid_helo_hostname, reject_non_fqdn_helo_hostname, reject_unknown_recipient_domain, reject_rbl_client zen.spamhaus.org, reject_rbl_client bl.spamcop.net, mysql:/etc/postfix/mysql-protected_users.cf, reject_non_fqdn_recipient, permit"

COPY postfix/mysql-email2email.cf /etc/postfix/mysql-email2email.cf
COPY postfix/mysql-protected_users.cf /etc/postfix/mysql-protected_users.cf
COPY postfix/mysql-virtual-alias-maps.cf /etc/postfix/mysql-virtual-alias-maps.cf
COPY postfix/mysql-virtual-lists-alias-maps.cf /etc/postfix/mysql-virtual-lists-alias-maps.cf
COPY postfix/mysql-virtual-mailbox-domains.cf /etc/postfix/mysql-virtual-mailbox-domains.cf
COPY postfix/mysql-virtual-mailbox-maps.cf /etc/postfix/mysql-virtual-mailbox-maps.cf
COPY postfix/mysql-virtual-system-alias-maps.cf /etc/postfix/mysql-virtual-system-alias-maps.cf
COPY postfix/mysql-virtual-verteiler-alias-maps.cf /etc/postfix/mysql-virtual-verteiler-alias-maps.cf

#ENV http_proxy=""
#ENV https_proxy=""

COPY ./start-mailserver-customized.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*

ENTRYPOINT /usr/local/bin/start-mailserver-customized.sh 
