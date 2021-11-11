# no libapache2-mod-macro in xenial
FROM ubuntu:trusty
MAINTAINER mwaeckerlin

ENV BASEPATH "/"
ENV LDAP_CONFIG_VERBOSE "1"
ENV LDAP_READ_DN ""
ENV LDAP_WRITE_DN ""
ENV LDAP_HOST ""
ENV LDAP_DOMAIN ""
ENV LDAP_BASE ""
ENV LDAP_USER_BASE ""
ENV LDAP_GROUP_BASE ""
ENV LDAP_URL ""
ENV LDAP_URL_QUERY "?uid?sub?(objectClass=posixAccount)"
ENV LDAP_BIND_DN ""
ENV LDAP_BIND_PWD ""
ENV LDAP_MEMBER_UID "memberUid"
ENV LDAP_GROUP_ATTR_IS_DN "off"

EXPOSE 80

RUN apt-get update
RUN apt-get install -y apache2 libapache2-mod-svn libapache2-mod-perl2 libnet-ldap-perl libapache2-mod-macro
RUN a2enmod dav_svn ldap authnz_ldap perl macro
ADD svn.conf /etc/apache2/conf-available/svn.conf
RUN a2enconf svn
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/2 /var/log/apache2/error.log
ADD start.sh /start.sh
CMD /start.sh

VOLUME /svn
