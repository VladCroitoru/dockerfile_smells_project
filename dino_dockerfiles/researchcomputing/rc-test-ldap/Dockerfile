FROM centos:7
MAINTAINER "Aaron Holt" <aaron.holt@colorado.edu>

ARG DOMAIN

RUN yum install -y epel-release \
    && yum update -y \
    && yum install -y 389-ds-base 389-adminutil \
    && yum clean all

COPY ${DOMAIN}/* /tmp/

# The 389-ds setup will fail because the hostname can't be reliably determined, so we'll bypass it and then install.
# Sleep command should be lengthened if you're getting ldap_sasl_bind(SIMPLE): Can't contact LDAP server (-1), ldap
# server hasn't started yet
RUN useradd ldapadmin \
   && rm -fr /var/lock /usr/lib/systemd/system \
   && sed -i 's/checkHostname {/checkHostname {\nreturn();/g' /usr/lib64/dirsrv/perl/DSUtil.pm \
   && sed -i 's/updateSelinuxPolicy($inf);//g' /usr/lib64/dirsrv/perl/* \
   && sed -i '/if (@errs = startServer($inf))/,/}/d' /usr/lib64/dirsrv/perl/* \
   && setup-ds.pl --silent --file /tmp/ds-setup.inf \
   && /usr/sbin/ns-slapd -D /etc/dirsrv/slapd-dir \
   && sleep 5 \
   && ldapadd -H ldap:/// -f /tmp/ldapconf.ldif -x -D "cn=Directory Manager" -w ${DOMAIN}_password

EXPOSE 389

CMD ["/bin/sh", "-c", "/usr/sbin/ns-slapd -D /etc/dirsrv/slapd-dir && tail -F /var/log/dirsrv/slapd-dir/access"]
