FROM fedora
MAINTAINER "Pedro Romero Aguado" <pedroromeroaguado@gmail.com> 

#installs
RUN dnf install -y procps openldap openldap-clients krb5-workstation cyrus-sasl-gssapi cyrus-sasl-ldap nss-pam-ldapd supervisor ; exit 0
# directoris
RUN mkdir /opt/docker

#Copy github to dockerhub build
COPY files /opt/docker
RUN cp -f /opt/docker/krb5.conf /etc/
RUN cp /opt/docker/supervisord.ini /etc/supervisord.d/
RUN cp /opt/docker/ns* /etc/
RUN cp -f /opt/docker/ldap.conf /etc/openldap/
#Copying tls files for SSL
RUN cp /opt/docker/ldapcert.pem /etc/openldap/certs/
RUN cp /opt/docker/ldapserver.pem /etc/openldap/certs/
RUN cp /opt/docker/cacert.pem /etc/ssl/certs/
RUN chmod 400 /etc/openldap/certs/ldapserver.pem
#VOLUME ["/data"] 
ENTRYPOINT ["/usr/bin/supervisord", "-c","/etc/supervisord.d/supervisord.ini"]
