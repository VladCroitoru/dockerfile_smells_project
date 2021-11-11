# Version 1.0.0
# cyan.org.LdapServer

#========== Basic Image ==========
From centos:7
MAINTAINER "DreamInSun"


#========== Evironment ==========
ENV LDAP_ADMIN_USER		ldapadmin
ENV LDAP_ADMIN_PASSWD	ldapadmin

ENV LDAP_URL			dc=ecoho,dc=cn	
ENV LDAP_SERVER_DOMAIN	ldap.ecoho.cn

ENV ADMIN_USER			admin
ENV ADMIN_PASSWD		123456


#========== Install EPEL & REMI ==========
ADD rpm /rpm 
RUN rpm --import /rpm/RPM-GPG-KEY-EPEL-7
RUN yum localinstall -y /rpm/epel-release-7-*.noarch.rpm
RUN rm -rf /rpm

#========== Edit Config ==========
#ADD etc         /etc

#========== Install 389 DirSrv ========== 
sudo yum install -y 389-ds-base 389-admin
sudo yum install -y idm-console-framework 389-adminutil 389-admin 389-admin-console 389-console 389-ds-console

#========== Expose ==========
EXPOSE 389
EXPOSE 636
EXPOSE 9830

#========= Initialiaze Shell ==========
ADD shell /shell
RUN chmod a+x /shell/*

#========== Entry Point ==========
RUN /shell/docker-entrypoint.sh
RUN cat /tmp/setup*.log

ENTRYPOINT ["/shell/docker-entrypoint.sh"]



