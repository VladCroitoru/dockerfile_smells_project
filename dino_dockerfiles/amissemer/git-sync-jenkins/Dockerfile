FROM jenkins/jenkins:2.107.2
MAINTAINER Adrien Missemer <adrien.missemer@gmail.com>

USER root
RUN apt-get update && apt-get install -y rsync && rm -rf /var/lib/apt/lists/*
USER jenkins

WORKDIR $JENKINS_HOME
ENV BASE_PLUGINS \
	build-user-vars \
	git \
	groovy
	
RUN install-plugins.sh $BASE_PLUGINS

COPY ref-config /usr/share/jenkins/ref
COPY entrypoint.sh  /usr/local/bin/
COPY upgrade /usr/local/bin/

# Default location of the Jenkins configuration files, from the root of the git repository (used by the commit-jenkins-config job)
# Can be overriden in child images or docker-compose.yml file
ENV JENKINS_CONFIG_PATH=jenkins-config

ENTRYPOINT ["tini", "--", "/usr/local/bin/entrypoint.sh"]
