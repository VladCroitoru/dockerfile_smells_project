FROM centos:centos6

MAINTAINER coleman <coleman_dlut@hotmail.com>

ENV MAILDOMAIN localhost
ENV TLS_CERT_FILE "/etc/pki/tls/certs/server.pem"
ENV TLS_KEY_FILE "/etc/pki/tls/certs/server.pem"


#************************************************************
#*  Updateし、postfix、cyrus-imapd、cyrus-sasl-md5、cyrus-saslをインストールする                       *
#************************************************************
RUN yum -y update && yum -y install postfix cyrus-imapd cyrus-sasl-md5 cyrus-sasl cyrus-sasl-plain && yum clean all


#/etc/imapd.confの変更
RUN sed -i -e "s/^admins: cyrus/admins: admin/" /etc/imapd.conf && \
sed -i -e "s/^sasl_pwcheck_method: saslauthd$/sasl_pwcheck_method: auxprop/" /etc/imapd.conf && \
sed -i -e "/^sasl_pwcheck_method: auxprop$/a sasl_auxprop_plugin: sasldb" /etc/imapd.conf && \
sed -i -e "s/^sasl_mech_list: PLAIN$/sasl_mech_list: LOGIN PLAIN CRAM-MD5 DIGEST-MD5/" /etc/imapd.conf && \
sed -i -e "s/^tls_cert_file: \/etc\/pki\/cyrus-imapd\/cyrus-imapd.pem/tls_cert_file: \/etc\/pki\/tls\/certs\/server.pem/" /etc/imapd.conf && \
sed -i -e "s/^tls_key_file: \/etc\/pki\/cyrus-imapd\/cyrus-imapd.pem/tls_key_file: \/etc\/pki\/tls\/certs\/server.pem/" /etc/imapd.conf && \
sed -i -e "s/^tls_ca_file: \/etc\/pki\/tls\/certs\/ca-bundle.crt/tls_ca_file: \/etc\/pki\/tls\/certs\/server.pem/" /etc/imapd.conf && \
sed -i -e "$ a allowanonymouslogin: no" /etc/imapd.conf && \
sed -i -e "$ a allowplaintext: yes" /etc/imapd.conf && \
sed -i -e "$ a autocreateinboxfolders: Sent|Draft|Trash" /etc/imapd.conf && \
sed -i -e "$ a autosubscribeinboxfolders: Sent|Draft|Trash" /etc/imapd.conf && \
sed -i -e "$ a virtdomains: on" /etc/imapd.conf && \
sed -i -e "$ a altnamespace: 1" /etc/imapd.conf && \
sed -i -e "$ a createonpost: 1" /etc/imapd.conf

#/etc/cyrus.confの変更
RUN sed -i -e "s/^  pop3\t\tcmd=\"pop3d\" listen=\"pop3\" prefork=3/# pop3\t\tcmd=\"pop3d\" listen=\"pop3\" prefork=3/" /etc/cyrus.conf && \
sed -i -e "s/^  pop3s\t\tcmd=\"pop3d -s\" listen=\"pop3s\" prefork=1/# pop3s\t\tcmd=\"pop3d -s\" listen=\"pop3s\" prefork=1/" /etc/cyrus.conf && \
sed -i -e "s/^  sieve\t\tcmd=\"timsieved\" listen=\"sieve\" prefork=0/# sieve\t\tcmd=\"timsieved\" listen=\"sieve\" prefork=0/" /etc/cyrus.conf && \
sed -i -e "$ i \ " /etc/cyrus.conf && \
sed -i -e "$ i \  # create SQUAT indexes for mailboxes" /etc/cyrus.conf && \
sed -i -e "$ i \  squatter      cmd=\"squatter -r -s user\" period=1440" /etc/cyrus.conf

#/etc/postfix/main.cfの変更
RUN sed -i -e "s/^#myhostname = virtual.domain.tld/myhostname = freemail.server-on.net/" /etc/postfix/main.cf && \
sed -i -e "s/^#mydomain = domain.tld/mydomain = freemail.server-on.net/" /etc/postfix/main.cf && \
sed -i -e "s/^inet_interfaces = localhost/inet_interfaces = all/" /etc/postfix/main.cf && \
sed -i -e "s/^inet_protocols = all/inet_protocols = ipv4/" /etc/postfix/main.cf && \
sed -i -e "s/^mydestination = \$myhostname, localhost.\$mydomain, localhost$/mydestination = \$myhostname, localhost.\$mydomain, localhost, \$mydomain/" /etc/postfix/main.cf && \
sed -i -e "s/^#local_recipient_maps =\$/local_recipient_maps =/" /etc/postfix/main.cf && \
sed -i -e "s/^#mailbox_transport = cyrus\$/mailbox_transport = cyrus/" /etc/postfix/main.cf && \
sed -i -e "s/^#fallback_transport =\$/fallback_transport = cyrus/" /etc/postfix/main.cf && \
sed -i -e "s/^#smtpd_banner = \$myhostname ESMTP \$mail_name\$/smtpd_banner = \$myhostname ESMTP unknown/" /etc/postfix/main.cf && \
sed -i -e "$ a \ " /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_sasl_auth_enable = yes" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_sasl_security_options = noanonymous" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_sasl_local_domain = \$myhostname" /etc/postfix/main.cf && \
sed -i -e "$ a broken_sasl_auth_clients=yes" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_use_tls = yes" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_tls_cert_file = /etc/pki/tls/certs/server.crt" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_tls_key_file = /etc/pki/tls/certs/server.key" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_tls_session_cache_database = btree:/var/lib/postfix/smtpd_scache" /etc/postfix/main.cf && \
sed -i -e "$ a smtpd_recipient_restrictions = permit_mynetworks,permit_sasl_authenticated,reject_unauth_destination" /etc/postfix/main.cf && \
sed -i -e "$ a mailbox_size_limit = 0" /etc/postfix/main.cf && \
sed -i -e "$ a message_size_limit = 0" /etc/postfix/main.cf

#/etc/sysconfig/saslauthdの変更
RUN sed -i -e 's/MECH=pam/MECH=rimap/' /etc/sysconfig/saslauthd && \
sed -i -e "s/FLAGS=/FLAGS='-r -O 127.0.0.1'/" /etc/sysconfig/saslauthd

#/etc/postfix/master.cfの変更
RUN sed -i -e "s/^#submission inet n/submission inet n/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_tls_security_level=encrypt/  -o smtpd_tls_security_level=may/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_sasl_auth_enable=yes/  -o smtpd_sasl_auth_enable=yes/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_client_restrictions=permit_sasl_authenticated,reject/  -o smtpd_client_restrictions=permit_sasl_authenticated,reject/" /etc/postfix/master.cf && \
sed -i -e "s/^#smtps     inet  n/smtps     inet  n/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_tls_wrappermode=yes/  -o smtpd_tls_wrappermode=yes/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_sasl_auth_enable=yes/  -o smtpd_sasl_auth_enable=yes/" /etc/postfix/master.cf && \
sed -i -e "s/^#  -o smtpd_client_restrictions=permit_sasl_authenticated,reject/  -o smtpd_client_restrictions=permit_sasl_authenticated,reject/" /etc/postfix/master.cf && \
sed -i -e "s/^#cyrus     unix  -       n/cyrus     unix  -       n/" /etc/postfix/master.cf && \
sed -i -e "s/^#  user=cyrus argv=\/usr\/lib\/cyrus-imapd\/deliver -e -r \${sender} -m \${extension} \${user}/  user=cyrus argv=\/usr\/lib\/cyrus-imapd\/deliver -e -r \${sender} -m \${extension} \${user}@\${domain}/" /etc/postfix/master.cf

RUN sed -i -e "s/^mech_list: plain login$/mech_list: LOGIN PLAIN CRAM-MD5 DIGEST-MD5/" /etc/sasl2/smtpd.conf

RUN touch /etc/sasldb2 && chmod 644 /etc/sasldb2 && \
    chown cyrus:mail /var/spool/imap/ && chmod 700 /var/spool/imap/ && \
    chown cyrus:mail /var/lib/imap/ && chmod 750 /var/lib/imap/

VOLUME  ["/var/spool/imap"]
VOLUME  ["/var/lib/imap"]

EXPOSE 25 587 465 143 993 

CMD bash -c "/sbin/service saslauthd start && /sbin/service postfix start && /sbin/service cyrus-imapd start && /bin/bash"

