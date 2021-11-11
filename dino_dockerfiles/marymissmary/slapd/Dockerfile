## apache server

FROM  debian:wheezy

MAINTAINER mary anne rohrdanz, marymissmary@gmail.com

## install ssh and supervisor
RUN apt-get update && apt-get install -y openssh-server supervisor
RUN mkdir -p  /var/run/sshd /var/log/supervisor

## install apache web server:
RUN apt-get update && apt-get install -y apache2
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor

## some other things I like to have:
RUN apt-get update && apt-get install -y vim curl

## set root password to something seriously challenging...
RUN echo 'root:root_password' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config


## install slapd in noninteractive mode
RUN echo 'slapd/root_password password password' | debconf-set-selections &&\
    echo 'slapd/root_password_again password password' | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils

## set up required inputs for configuration of slapd
## debconf-set-selections is used so that we can run dpkg-reconfigure
## noninteractively below
RUN echo "slapd slapd/no_configuration boolean false" | debconf-set-selections
RUN echo "slapd slapd/domain string ldaptest.local" | debconf-set-selections
RUN echo "slapd shared/organization string 'LDAP Test'" | debconf-set-selections
RUN echo "slapd slapd/password1 password root_password" | debconf-set-selections
RUN echo "slapd slapd/password2 password root_password" | debconf-set-selections
RUN echo "jslapd slapd/backend select HDB" | debconf-set-selections
RUN echo "slapd slapd/purge_database boolean true" | debconf-set-selections
RUN echo "slapd slapd/allow_ldap_v2 boolean false" | debconf-set-selections
RUN echo "slapd slapd/move_old_database boolean true" | debconf-set-selections

RUN dpkg-reconfigure -f noninteractive slapd


COPY config_files/ldap.conf     /etc/ldap/ldap.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY config_files/vimrc           /root/.vimrc
COPY config_files/alias           /root/.alias
COPY config_files/bashrc          /root/.bashrc


EXPOSE 22 80 
EXPOSE 389

## file of data to pupulate the database:
COPY ldif_files/testdata.ldif   /root/testdata.ldif


CMD ["/usr/bin/supervisord"]
