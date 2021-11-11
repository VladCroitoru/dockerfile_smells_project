FROM jenkins

MAINTAINER Victor Seva <linuxmaniac@torreviejawireless.org>

USER root

COPY jdg.list /etc/apt/sources.list.d/jdg.list

RUN wget -O - http://jenkins.grml.org/debian/C525F56752D4A654.asc | apt-key add -

RUN apt-get update && apt-get install -y \
	jenkins-debian-glue-buildenv curl pep8 libperl-critic-perl shellcheck && \
	rm -rf /var/lib/apt/lists/*

COPY jenkins_sudo /etc/sudoers.d/jenkins
RUN chmod 440 /etc/sudoers.d/jenkins

# uncomment this block for use approx in host
#ENV DOCKER_IP 172.17.42.1
#ENV APPROX_PORT 9999
#ENV JENKINS_UC_DOWNLOAD http://${DOCKER_IP}:${APPROX_PORT}/jenkins_plugins/
#COPY pbuilderrc /etc/pbuilderrc
##

# root of repositories as volumen so it
# can be persisted and survive image upgrades
VOLUME /srv/repository
RUN chown -R jenkins /srv/repository

USER jenkins

COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
