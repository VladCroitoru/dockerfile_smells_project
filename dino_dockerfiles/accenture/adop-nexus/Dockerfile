FROM sonatype/nexus3:3.17.0


ENV LDAP_ENABLED=true \
    NEXUS_CONTEXT=nexus \
    DEBUG_LOGGING=false \
    LDAP_SEARCH_BASE="" \
    LDAP_NAME=nexusldap \
    LDAP_URL="" \
    LDAP_PORT=389 \
    LDAP_AUTH_PROTOCOL=ldap \
    LDAP_AUTH_SCHEME=simple \
    LDAP_USER_EMAIL_ATTRIBUTE=mail \
    LDAP_GROUPS_AS_ROLES=true \
    LDAP_GROUP_BASE_DN=ou=groups \
    LDAP_GROUP_ID_ATTRIBUTE=cn \
    LDAP_GROUP_MEMBER_ATTRIBUTE=uniqueMember \
    LDAP_GROUP_OBJECT_CLASS=groupOfUniqueNames \
    LDAP_PREFERRED_PASSWORD_ENCODING=crypt \
    LDAP_MAP_GROUP_AS_ROLES=true \
    LDAP_USER_ID_ATTRIBUTE=uid \
    LDAP_USER_PASSWORD_ATTRIBUTE=userPassword \
    LDAP_USER_OBJECT_CLASS=inetOrgPerson \
    LDAP_USER_BASE_DN=ou=people \
    LDAP_USER_REAL_NAME_ATTRIBUTE=cn \
    LDAP_GROUP_MEMBER_FORMAT='${dn}' \
    NEXUS_CREATE_CUSTOM_ROLES=false \
    NEXUS_JMX_PASSWORD=adopnexusjmx \
    DOCKERIZE_VERSION=v0.6.1

USER root

RUN yum install -y epel-release

RUN yum install -y \
    yum-plugin-fastestmirror-1.1.31-50.el7 \
    yum-utils-1.1.31-50.el7 \
    yum-plugin-ovl-1.1.31-50.el7 \
    systemd-libs-219-62.el7_6.6 \
    systemd-219-62.el7_6.6 \
    gnupg2-2.0.22-5.el7_5 \
    bind-license-9.9.4-74.el7_6.1Z \
    zip \
    unzip \
    which \
    jq

RUN curl -s get.sdkman.io | bash
RUN source "$HOME/.sdkman/bin/sdkman-init.sh"
RUN yes | /bin/bash -l -c "sdk install groovy 2.4.17"

RUN curl -Ls https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar -C /usr/local/bin -xz

ENV PATH="/root/.sdkman/candidates/groovy/2.4.17/bin:${PATH}"
RUN export PATH

COPY resources/nexus.sh /usr/local/bin/
COPY resources/provision.sh /usr/local/bin/
COPY resources/ /resources/
COPY resources/conf/grapeConfig.xml /root/.groovy/

RUN grape install org.jboss.spec.javax.ws.rs jboss-jaxrs-api_2.0_spec 1.0.1.Final \
    && grape install org.jboss.spec.javax.servlet jboss-servlet-api_3.1_spec 1.0.2.Final \
    && grape install org.jboss.spec.javax.annotation jboss-annotations-api_1.2_spec 1.0.2.Final \
    && grape install javax.activation activation 1.1 \
    && grape install net.jcip jcip-annotations 1.0 \
    && grape install org.jboss.logging jboss-logging-annotations 2.2.0.Final \
    && grape install org.jboss.logging jboss-logging-processor 2.2.0.Final \
    && grape install com.sun.xml.bind jaxb-impl 2.3.2 \
    && grape install org.apache.james apache-mime4j 0.6.1 \
    && grape install org.sonatype.nexus nexus-rest-client 3.17.0-01 \
    && grape install org.sonatype.nexus nexus-rest-jackson2 3.17.0-01 \
    && grape install org.sonatype.nexus nexus-script 3.17.0-01 \
    && grape install com.fasterxml.jackson.core jackson-core 2.9.2 \
    && grape install com.fasterxml.jackson.core jackson-databind 2.9.2 \
    && grape install com.fasterxml.jackson.core jackson-annotations 2.9.2 \
    && grape install com.fasterxml.jackson.jaxrs jackson-jaxrs-json-provider 2.9.2 \
    && grape install javax.activation activation 1.1 \
    && grape install net.jcip jcip-annotations 1.0 \
    && grape install org.jboss.logging jboss-logging-annotations 2.2.0.Final \
    && grape install org.jboss.logging jboss-logging-processor 2.2.0.Final \
    && grape install com.sun.xml.bind jaxb-impl 2.3.2 \
    && grape install com.sun.mail javax.mail 1.6.1

RUN chmod u+x /usr/local/bin/nexus.sh && chmod u+x /usr/local/bin/provision.sh

ENTRYPOINT ["/usr/local/bin/nexus.sh"]
