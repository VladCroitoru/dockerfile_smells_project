FROM centos:7

# Jenkins will be running on a Mesos cluster, add mesos libs in addition to the usual packages
RUN rpm -Uvh http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-repo-7-2.noarch.rpm && \
    rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
	curl http://pkg.jenkins-ci.org/redhat/jenkins.repo > /etc/yum.repos.d/jenkins.repo && \
	rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key && \
	yum -y install curl git java-1.8.0-openjdk jenkins jq mesos unzip zip && \
	yum -y update && \
	yum clean all

# For the main web interface
EXPOSE 8080

# Used by build workers
EXPOSE 50000

ENV JENKINS_HOME=/var/lib/jenkins

COPY scripts/run-jenkins.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run-jenkins.sh

COPY scripts/init-plugins.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/init-plugins.sh

COPY scripts/bootstrap.py /usr/local/bin/
RUN chmod +x /usr/local/bin/bootstrap.py

COPY conf/config.xml /usr/local/src/jenkins-config.xml

ENTRYPOINT [ "/usr/local/bin/run-jenkins.sh" ]
