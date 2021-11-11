FROM centos:centos6

MAINTAINER coleman <coleman_dlut@hotmail.com>

ENV MAIL_SERVER_DOMAIN_NAME freemail.server-on.net
ENV TLS_CERT_FILE "/etc/pki/tls/certs/server.pem"
ENV TLS_KEY_FILE "/etc/pki/tls/certs/server.pem"

#************************************************************
#*  Updateし、postfix、cyrus-imapd、cyrus-sasl-md5、cyrus-saslをインストールする                       *
#************************************************************
RUN yum -y update && yum -y install postfix dovecot && yum clean all

RUN useradd vmail && \
sed -i -e "s/\/home\/vmail:\/bin\/bash/\/var\/spool\/virtual:\/sbin\/nologin/" /etc/passwd && \
mkdir /var/spool/virtual

ADD start.sh /opt/start.sh
RUN chmod 700 /opt/start.sh

CMD /opt/start.sh



