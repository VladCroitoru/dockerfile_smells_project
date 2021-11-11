FROM centos:7

MAINTAINER Donald Simpson <donaldsimpson@gmail.com>
### This is a CentOS/RHEL 7 Docker image for Jenkins
### TODO: Sort out the jenkins user
### Jenkins User and Group setup:
### Not being used yet...
ARG CONTAINER_UID=1000
ARG CONTAINER_GID=1000

# - Jenkins start script & init process
COPY jenkins.sh /usr/local/bin/jenkins.sh
COPY tini /bin/

### Combine yum update with all yum install commands:
RUN yum update -y \
	&& yum install -y java-1.8.0-openjdk-devel \
	&& yum install -y git \
	&& yum install -y python \
	&& yum install -y docker \
	&& yum install -y wget \
	&& yum install -y which \
	&& yum clean all \
	&& rm -rf /var/cache/yum \
	&& export CONTAINER_USER=jenkins \
	&& export CONTAINER_GROUP=jenkins \
	&& /usr/sbin/groupadd --gid $CONTAINER_GID jenkins \
	&& /usr/sbin/useradd --uid $CONTAINER_UID --gid $CONTAINER_GID --create-home --shell /bin/bash jenkins \
	&& mkdir /var/jenkins_home \
	&& mkdir /usr/share/jenkins \
	&& cd /usr/share/jenkins \
	&& rm -rf /var/cache/yum \
	&& wget --no-check-certificate http://mirrors.jenkins-ci.org/war/latest/jenkins.war \
	&& chmod +x /bin/tini \
	&& chmod +x /usr/local/bin/jenkins.sh \
	&& chown -R jenkins:jenkins /var/jenkins_home 

### EXPOSED PORTS - 8080 for web interface and 5000 for JNLP slave nodes:
EXPOSE 8080 50000

### ENV VARIBALES:
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

### EXPOSE VOLUME
VOLUME /var/jenkins_home

#Not working yet... 
#USER jenkins

### ENTRYPOINT - use script to manage the Jenkins process, and tini to manage the script
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
