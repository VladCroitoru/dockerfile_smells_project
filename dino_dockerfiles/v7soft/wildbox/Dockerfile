FROM ubuntu

RUN apt-get update ; \
 echo "postfix postfix/mailname string wildbox.catcher" | debconf-set-selections ;\
 echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections ;\
 echo "postfix postfix/mynetworks      string  0.0.0.0/0" | debconf-set-selections ;\
 echo "dovecot-core    dovecot-core/create-ssl-cert    boolean false" | debconf-set-selections ;\
 echo "dovecot-core    dovecot-core/ssl-cert-name      string  localhost" | debconf-set-selections ;\
 DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -o Acquire::ForceIPv4=true postfix dovecot-imapd postfix-pcre mailutils ;\
 echo -en "NO\n.\n.\nDovecot mail server\nlocalhost\n\localhost\no@localhost\n"|openssl req -newkey rsa:2048  -x509 -days 3652.5 -nodes -rand /dev/urandom \
 -out /etc/dovecot/dovecot.pem -keyout /etc/dovecot/private/dovecot.pem ;\
 useradd wildbox ;\
 echo "wildbox:wildbox" | chpasswd ;\
 postconf -e virtual_alias_maps=pcre:/etc/postfix/virtual_alias.pcre ;\
 postconf -e luser_relay=wildbox ;\
 postconf -e local_recipient_maps= ;\
 postconf -e 'mydestination=$myhostname, pcre:/etc/postfix/mydestination.pcre' ;\
 echo "/.*/    OK" >> /etc/postfix/mydestination.pcre ;\
 echo "/\/@/ wildbox" > /etc/postfix/virtual_alias.pcre ;\
 mkdir /home/wildbox ;\
 chown wildbox:wildbox /home/wildbox/

EXPOSE 25/tcp 143/tcp 993/tcp 

CMD dovecot;/usr/lib/postfix/master -d -c /etc/postfix

