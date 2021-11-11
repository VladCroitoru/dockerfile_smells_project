FROM valtri/docker-midpoint
MAINTAINER František Dvořák

ENV tag v1.0.0
ENV tag_sample bb74aa058ed73d027c16a273d29b63822a9f0536
ENV pass 5ecr3t
ENV REALM UNDERGROUND
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends krb5-admin-server krb5-kdc curl \
 && rm -rf /var/lib/apt/lists/*

COPY kadm5.acl /etc/krb5kdc/kadm5.acl

RUN echo "DAEMON_ARGS=\"-r $REALM\"" > /etc/default/krb5-kdc \
 && echo "DAEMON_ARGS=\"-r $REALM\"" > /etc/default/krb5-admin-server

RUN mv /docker-entry.sh /docker-entry-base.sh
COPY docker-entry.sh /
RUN sed -i /docker-entry.sh -e "s/^\(REALM\)=.*/\1=${REALM}/"

RUN wget -nv https://github.com/CESNET/kerberos-connector/releases/download/${tag}/debian-9.tar \
 && tar xf debian-9.tar \
 && mkdir -p /opt/kerberos \
 && cp -vp debian-9/libkerberos-connector.so /opt/kerberos \
 && cp -vp debian-9/kerberos-connector-*.jar /var/opt/midpoint/icf-connectors \
 && rm -rf debian-9/ debian-9.tar \
 && echo 'JAVA_OPTS="${JAVA_OPTS} -Djava.library.path=/opt/kerberos"' >> /etc/default/tomcat8

RUN wget -nv https://raw.githubusercontent.com/CESNET/kerberos-connector/${tag_sample}/samples/kerberos.xml \
 && sed -i kerberos.xml \
   -e "s,\$(kerberosRealm),$REALM,g" \
   -e "s,\$(kerberosPrincipal),admin/admin@$REALM," \
   -e "s,\$(kerberosKeytab),/etc/tomcat8/idm.keytab," \
   -e "s,\$(kerberosLifeTime),3600000,"

# import the resource
RUN rm -fv /var/log/tomcat8/idm*.log \
 && service tomcat8 start || : \
 && i=0; while ! grep 'org\.apache\.wicket\.protocol\.http\.WebApplication.*Started Wicket' /var/log/tomcat8/idm.log && test $i -lt 120; do i=$((i+1)); echo "sleep $i"; sleep 1; done \
 && curl -i --user administrator:${pass} -H "Content-Type: application/xml" -X POST http://localhost:8080/midpoint/ws/rest/resources -d @kerberos.xml \
  && sleep 60
