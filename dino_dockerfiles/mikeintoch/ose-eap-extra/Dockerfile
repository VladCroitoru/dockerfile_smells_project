FROM registry.access.redhat.com/jboss-eap-6/eap64-openshift

ADD gradle_scripts /tmp/gradle_scripts

USER root

RUN [ "bash", "-x", "/tmp/gradle_scripts/install.sh" ]
RUN rm -rf /tmp/gradle_scripts

USER 185

RUN touch /opt/eap/I_AM_HERE_v01
