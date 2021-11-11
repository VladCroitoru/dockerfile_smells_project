FROM fedora:22
MAINTAINER Ermanno Scaglione <erm67@yahoo.it>
RUN dnf -y update && dnf -y install httpd mod_ssl mod_xsendfile php php-tidy php-opcache php-xml php-pecl-zip php-pdo php-mysqlnd php-mbstring php-ldap php-intl php-gd php-cli php-bcmath php-pecl-imagick php-pecl-apcu php-pecl-zip php-gmp php-imap php-mcrypt php-xml php-xmlrpc && dnf clean all
EXPOSE 80 443
VOLUME ["/var/www/", "/var/log/httpd", "/etc/httpd/" \
        "/etc/pki/tls/certs/localhost.crt", "/etc/pki/tls/private/localhost.key"]

ADD run-apache.sh /run-apache.sh
RUN chmod -v +x /run-apache.sh

CMD ["/run-apache.sh"]
