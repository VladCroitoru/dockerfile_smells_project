FROM fedora
MAINTAINER "Antonia Aguado Mercado" <nomail@gmail.com> 

#installs
RUN dnf install -y procps openldap openldap-servers openldap-clients krb5-workstation krb5-server-ldap cyrus-sasl-gssapi cyrus-sasl-ldap nss-pam-ldapd 
# directoris
RUN mkdir /opt/docker
RUN mkdir /var/tmp/home
RUN mkdir /var/tmp/home/1asix
RUN mkdir /var/tmp/home/2asix
#Copy github to dockerhub build
COPY scripts /scripts/
COPY files /opt/docker
RUN cp /opt/docker/ns* /etc/
RUN cp -f /opt/docker/ldap.conf /etc/openldap/
RUN cp -f /opt/docker/krb5.conf /etc/
#Copying tls files for SSL
#RUN cp /opt/docker/ca_server.pem /etc/openldap/certs/
RUN cp /opt/docker/ldapcert.pem /etc/openldap/certs/
RUN cp /opt/docker/ldapserver.pem /etc/openldap/certs/
RUN cp /opt/docker/cacert.pem /etc/ssl/certs/
RUN chmod 400 /etc/openldap/certs/ldapserver.pem
#RUN chown ldap.ldap /etc/openldap/certs/*
RUN cp /opt/docker/krb5.keytab /etc/
RUN chmod 640 /etc/krb5.keytab
RUN setfacl -m u:ldap:r /etc/krb5.keytab
#RUN setfacl -m u:ldap:r /etc/pki/tls/private/slapd.pem
RUN cp /usr/share/doc/krb5-server-ldap/kerberos.schema /etc/openldap/schema/
#COPY configs /etc/
#make executable and execute
RUN /usr/bin/chmod +x /scripts/startup-slapd.sh & bash /scripts/startup-slapd.sh ; exit 0
#VOLUME ["/data"] 
ENTRYPOINT /usr/sbin/nslcd & /usr/sbin/slapd & /bin/bash
EXPOSE 25 143 587 993 4190 8001 8002 9001 389
