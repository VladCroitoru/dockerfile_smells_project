FROM owncloud:latest
MAINTAINER Brendan Smithyman <brendan@bitsmithy.net>

RUN apt-get update && apt-get install -y php5-ldap libldap2-dev libldb-dev smbclient
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap*.so /usr/lib/
RUN docker-php-ext-install ldap
RUN docker-php-ext-install ftp
