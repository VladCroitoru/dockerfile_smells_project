FROM freeipa/freeipa-server

# /var /log is a symbolic link to /data/var/log
# Cannot install java without removing the link
RUN rm /var/log
RUN mkdir -p /var/log

RUN yum -y install java-1.8.0-openjdk-devel

RUN mkdir /keycloak-work
ADD https://downloads.jboss.org/keycloak/3.4.3.Final/keycloak-demo-3.4.3.Final.tar.gz /keycloak-work/keycloak-dist/
ADD freeipa-realm.json /keycloak-work/freeipa-realm.json
ADD keycloak-freeipa-trigger.sh /keycloak-work/keycloak-freeipa-trigger.sh

RUN chmod -v +x /keycloak-work/keycloak-freeipa-trigger.sh

ENTRYPOINT /keycloak-work/keycloak-freeipa-trigger.sh
