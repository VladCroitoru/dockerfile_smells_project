FROM fedora
MAINTAINER "Pedro Romero Aguado" <pedroromeroaguado@gmail.com> 

#installs
RUN dnf install -y procps openldap openldap-servers openldap-clients krb5-workstation krb5-server-ldap supervisor nss-pam-ldapd ; exit 0
# directoris
RUN mkdir /opt/docker
#Copy github to dockerhub build
COPY scripts /scripts/
COPY files /opt/docker
RUN cp /opt/docker/supervisord.ini /etc/supervisord.d/
RUN cp /opt/docker/ns* /etc/
RUN cp -f /opt/docker/ldap.conf /etc/openldap/
RUN cp -f /opt/docker/krb5.conf /etc/
#Copying tls files for SSL
#RUN cp /opt/docker/ca_server.pem /etc/openldap/certs/
RUN cp /opt/docker/ldapcert.pem /etc/openldap/certs/
RUN cp /opt/docker/ldapserver.pem /etc/openldap/certs/
RUN cp /opt/docker/cacert.pem /etc/ssl/certs/
RUN chmod 400 /etc/openldap/certs/ldapserver.pem
#make executable and execute
RUN /usr/bin/chmod +x /scripts/startup-slapd.sh && bash /scripts/startup-slapd.sh ; exit 0
#VOLUME ["/data"] 
ENTRYPOINT ["/usr/bin/supervisord", "-c","/etc/supervisord.d/supervisord.ini"]
