FROM jboss/keycloak-postgres:latest

RUN sed -ie 's@\(redirect-socket="https"\)@\1 proxy-address-forwarding="true"@' /opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && sed -ie 's@\(</dependencies>\)@    <module name="org.postgresql.jdbc"/>\n    \1@' /opt/jboss/keycloak/modules/system/layers/base/org/jgroups/main/module.xml

ADD changeJGroups.xsl /opt/jboss/keycloak/

RUN java -jar /usr/share/java/saxon.jar -s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml -xsl:/opt/jboss/keycloak/changeJGroups.xsl -o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml; rm /opt/jboss/keycloak/changeJGroups.xsl

ADD docker-entrypoint.sh /opt/jboss/

CMD ["--server-config", "standalone-ha.xml"]
