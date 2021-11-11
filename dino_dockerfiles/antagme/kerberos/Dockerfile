FROM fedora
MAINTAINER "Pedro Romero Aguado" <pedroromeroaguado@gmail.com> 

#installs
RUN dnf install -y krb5-server krb5-workstation nss-pam-ldapd supervisor procps ; exit 0
# directoris
RUN mkdir /opt/docker
#Copy github to dockerhub build
COPY scripts /scripts/
COPY files /opt/docker
#FOR TAKE hosts from ldap
RUN cp -r /opt/docker/ns* /etc
RUN cp -f /opt/docker/supervisord.ini /etc/supervisord.d/
#CPING FILES TO DESTINY DIRECTORIS
RUN cp -f /opt/docker/krb5.* /etc/
#RUN chown root:root /etc/krb5.conf
#RUN chmod 644 /etc/krb5.conf 
#FIRSTLY DO KDB5_UTIL!!!
RUN bash /scripts/kdb5_init.sh
#CONTINUE COPYING
RUN cp -f /opt/docker/kdc.conf /var/kerberos/krb5kdc/
RUN cp -f /opt/docker/kadm5.acl /var/kerberos/krb5kdc/
RUN bash /scripts/local_admin.sh
RUN cp -f /opt/docker/principal* /var/kerberos/krb5kdc/
#RUN chown -R root:root /var/kerberos/krb5kdc/
#RUN chmod 600 /var/kerberos/krb5kdc/kd*
#START DEMONS
#RUN /usr/sbin/krb5kdc && /usr/sbin/kadmind
#COPY configs /etc/
#make executable and execute
#VOLUME ["/data"] 
ENTRYPOINT ["/usr/bin/supervisord", "-c","/etc/supervisord.d/supervisord.ini"]
