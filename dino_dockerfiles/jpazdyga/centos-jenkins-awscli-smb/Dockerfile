FROM jpazdyga/centos7-base

MAINTAINER Jakub Pazdyga <pazdyga@pythian.com>

ENV container docker
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000
ENV DATE_TIMEZONE UTC
ENV JENKINS_VERSION 1.642.2
ENV JENKINS_SHA e72e06e64d23eefb13090459f517b0697aad7be0
ENV JENKINS_UC https://updates.jenkins-ci.org
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

RUN rpmdb --rebuilddb && \ 
    rpmdb --initdb && \
    yum clean all && \
    yum -y update && \
    yum -y install wget \ 
		   curl \
		   bind-utils \
		   screen \
		   openssl-devel \
		   gcc \
		   make \
		   java \
		   openldap-devel \
		   openssh \
                   openssl \ 
                   openssl-libs \
                   psmisc \
		   python \
		   samba-client \
 		   samba-client-libs \
		   samba-common-tools \
		   samba-libs \
		   samba
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
VOLUME /var/jenkins_home
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref

# could use ADD but this one does not check Last-Modified header 
# see https://github.com/docker/docker/issues/8331
RUN curl -fL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war \
  && echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -

RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install awscli

RUN wget https://gp2x.org/adtool/adtool-1.3.3.tar.gz
RUN tar -zxvf adtool-1.3.3.tar.gz ; cd adtool-1.3.3; ./configure; make; make install; cp src/etc/adtool.cfg.dist /usr/local/etc/adtool.cfg

# Use tini as subreaper in Docker container to adopt zombie processes
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini \
  && echo "$TINI_SHA /bin/tini" | sha1sum -c -

USER jenkins

COPY jenkins.sh /usr/local/bin/jenkins.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

COPY plugins.sh /usr/local/bin/plugins.sh

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000
