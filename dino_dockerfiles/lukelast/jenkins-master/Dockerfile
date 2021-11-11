FROM jenkins

# Install a base set of plugins.
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

#These directories must be created by root.
USER root

# This directory will replace ${ITEM_ROOTDIR}/builds
RUN mkdir /var/jenkins_builds && chown jenkins:jenkins /var/jenkins_builds

# This directory will replace ${ITEM_ROOTDIR}/workspace
RUN mkdir /var/jenkins_workspace && chown jenkins:jenkins /var/jenkins_workspace

USER jenkins

VOLUME /var/jenkins_builds
#VOLUME /var/jenkins_workspace

COPY config/* "$JENKINS_HOME"/
USER root
RUN chown -R jenkins "$JENKINS_HOME"
USER jenkins