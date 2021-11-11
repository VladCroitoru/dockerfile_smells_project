FROM centos:centos7.6.1810

# Java Env Variables
ENV JAVA_VERSION=1.8.0_202
ENV JAVA_TARBALL=server-jre-8u202-linux-x64.tar.gz
ENV JAVA_HOME=/opt/java/jdk${JAVA_VERSION}

# Swarm Env Variables (defaults)
ENV SWARM_MASTER=http://jenkins:8080/jenkins/
ENV SWARM_USER=jenkins
ENV SWARM_PASSWORD=jenkins

# Slave Env Variables
ENV SLAVE_NAME="Swarm_Slave"
ENV SLAVE_LABELS="docker aws ldap"
ENV SLAVE_MODE="exclusive"
ENV SLAVE_EXECUTORS=1
ENV SLAVE_DESCRIPTION="Core Jenkins Slave"

# Pre-requisites
RUN yum -y install epel-release
RUN yum install -y which \
    git \
    wget \
    tar \
    zip \
    unzip \
    openldap-clients \
    openssl \
    python-pip \
    systemd-219-62.el7_6.2.x86_64 \
    systemd-libs-219-62.el7_6.2.x86_64 \
    libxslt && \
    yum clean all 

RUN pip install awscli==1.10.19

# Docker versions Env Variables
ENV DOCKER_ENGINE_VERSION=1.10.3-1.el7.centos
ENV DOCKER_COMPOSE_VERSION=1.6.0
ENV DOCKER_MACHINE_VERSION=v0.6.0

RUN curl -fsSL https://get.docker.com/ | sed "s/docker-engine/docker-engine-${DOCKER_ENGINE_VERSION}/" | sh

RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose
RUN curl -L https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
    chmod +x /usr/local/bin/docker-machine

# Install Java
RUN wget -q --no-check-certificate --directory-prefix=/tmp \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
            https://download.oracle.com/otn-pub/java/jdk/8u202-b08/1961070e4c9b4e26a04e7f5a083f551e/${JAVA_TARBALL} && \
          mkdir -p /opt/java && \
              tar -xzf /tmp/${JAVA_TARBALL} -C /opt/java/ && \
            alternatives --install /usr/bin/java java /opt/java/jdk${JAVA_VERSION}/bin/java 100 && \
                rm -rf /tmp/* && rm -rf /var/log/*

# Make Jenkins a slave by installing swarm-client
RUN curl -s -o /bin/swarm-client.jar -k http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/2.0/swarm-client-2.0-jar-with-dependencies.jar

# Start Swarm-Client
CMD java -jar /bin/swarm-client.jar -executors ${SLAVE_EXECUTORS} -description "${SLAVE_DESCRIPTION}" -master ${SWARM_MASTER} -username ${SWARM_USER} -password ${SWARM_PASSWORD} -name "${SLAVE_NAME}" -labels "${SLAVE_LABELS}" -mode ${SLAVE_MODE}
