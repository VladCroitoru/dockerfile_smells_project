FROM sherl0cks/docker-eap:latest

####### MAINTAINER ############
MAINTAINER "Justin Holmes" "jholmes@redhat.com"


####### INSTALL PACKAGES #######
USER root
RUN yum install -y git && yum clean all
USER jboss


####### BPMS ARTIFACT #######
ENV ARTIFACT_REPOSITORY http://files.justinholmes.co
ENV BPMS_VERSION 6.4.0.GA

ADD jboss-bpmsuite-$BPMS_VERSION-deployable-eap6.x.zip /opt/jboss/


RUN cd /opt/jboss/ \
# && curl -O $ARTIFACT_REPOSITORY/jboss-bpmsuite-$BPMS_VERSION-deployable-eap6.x.zip \
 && unzip -q -o jboss-bpmsuite-$BPMS_VERSION-deployable-eap6.x.zip -d .  \
 &&	rm jboss-bpmsuite-$BPMS_VERSION-deployable-eap6.x.zip


####### EAP CONFIG #######
RUN curl https://raw.githubusercontent.com/sherl0cks/ansible-openstack-etc/53e733739dece3223ecaa6554dea62e5b68d1609/ansible/files/application-roles.properties > $JBOSS_HOME/standalone/configuration/application-roles.properties \
 &&	curl https://raw.githubusercontent.com/sherl0cks/ansible-openstack-etc/cb56b5eb0b23520960671d818ab94af82f0dece7/ansible/files/application-users.properties > $JBOSS_HOME/standalone/configuration/application-users.properties \
 &&	curl https://raw.githubusercontent.com/sherl0cks/ansible-openstack-etc/master/ansible/files/mgmt-groups.properties > $JBOSS_HOME/standalone/configuration/mgmt-groups.properties \
 &&	curl https://raw.githubusercontent.com/sherl0cks/ansible-openstack-etc/master/ansible/files/mgmt-users.properties > $JBOSS_HOME/standalone/configuration/mgmt-users.properties


####### MAVEN CONFIG #######
RUN mkdir -p /opt/jboss/.m2 \
 && curl https://raw.githubusercontent.com/sherl0cks/ansible-openstack-etc/852ff4a423b147eab7d2025e51e0294214676c20/ansible/files/settings.xml > /opt/jboss/.m2/settings.xml

####### SSH GITHOOK CONFIG #######
RUN mkdir -p /opt/jboss/.ssh \
 && chmod 755 /opt/jboss/.ssh

####### FILE PERMISSIONS #######
RUN mkdir /opt/jboss/.niogit \
 && chmod -R a+rw /opt/jboss/.niogit \
 && mkdir /opt/jboss/repositories \
 && chmod -R a+rw /opt/jboss/repositories \
 && mkdir /opt/jboss/.index \
 && chmod -R a+rw /opt/jboss/.index


####### JAVA_OPTS #######
ENV JAVA_OPTS -Dkie.maven.settings.custom=/opt/jboss/.m2/settings.xml \
	-Djboss.bind.address=0.0.0.0 \
	-Djboss.bind.address.management=0.0.0.0 \
    -Dorg.uberfire.nio.git.daemon.host=0.0.0.0 \
	-Dorg.uberfire.nio.git.ssh.host=0.0.0.0 \
	-Djava.security.egd=file:/dev/./urandom \
	-Dorg.uberfire.nio.git.ssh.cert.dir=/opt/jboss/.ssh


####### PORTS #######
EXPOSE 8080 9990 9418 8001

COPY startJBossWithOptions.sh /opt/jboss/jboss-eap-6.4/bin/

CMD ["/opt/jboss/jboss-eap-6.4/bin/startJBossWithOptions.sh"]