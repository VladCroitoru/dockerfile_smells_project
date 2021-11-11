FROM ubuntu:trusty

#install jdk8
RUN apt-get update && \
#    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean&& \ 
    apt-get install oracle-java8-set-default

RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get update && apt-get install -y --no-install-recommends wget git curl zip make g++-4.9 cmake && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/gcc-4.9 /usr/bin/gcc
RUN ln -s /usr/bin/g++-4.9 /usr/bin/g++
RUN ln -s /usr/bin/gcc /usr/bin/cc
RUN ln -s /usr/bin/g++ /usr/bin/c++

RUN update-ca-certificates -f

ENV JENKINS_HOME /var/jenkins_home

# Jenkins is ran with user `jenkins`, uid = 1000
# If you bind mount a volume from host/vloume from a data container,
# ensure you use same uid
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins

# Jenkins home directoy is a volume, so configuration and build history
# can be persisted and survive image upgrades
VOLUME /var/jenkins_home

# `/usr/share/jenkins/ref/` contains all reference configuration we want
# to set on a fresh new installation. Use it to bundle additional plugins
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

# Use tini as subreaper in Docker container to adopt zombie processes
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

# jenkins version being bundled in this docker image
ARG JENKINS_VERSION
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.60.3}

# jenkins.war checksum, download will be validated using it
ARG JENKINS_SHA=2d71b8f87c8417f9303a73d52901a59678ee6c0eefcf7325efed6035ff39372a

# Can be used to customize where jenkins.war get downloaded from
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war
# could use ADD but this one does not check Last-Modified header neither does it allow to control checksum 
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \
  && echo "${JENKINS_SHA}  /usr/share/jenkins/jenkins.war" | sha256sum -c -

#ENV JENKINS_VERSION 1.651.3
#ENV JENKINS_SHA 564e49fbd180d077a22a8c7bb5b8d4d58d2a18ce

# could use ADD but this one does not check Last-Modified header
# see https://github.com/docker/docker/issues/8331
#RUN curl -fL http://mirrors.jenkins-ci.org/war-stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \
#  && echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -

ENV JENKINS_UC https://updates.jenkins-ci.org
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

# Install docker-engine
# According to Petazzoni's article:
# ---------------------------------
# "Former versions of this post advised to bind-mount the docker binary from
# the host to the container. This is not reliable anymore, because the Docker
# Engine is no longer distributed as (almost) static libraries."
#ARG docker_version=1.11.2
RUN curl -sSL https://get.docker.com/ | sh && \
    apt-get purge -y docker-ce && \
    apt-get install docker-ce

# Make sure jenkins user has docker privileges
RUN usermod -aG docker jenkins
# allow jenkins to run sudo
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Installing node
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs


USER jenkins

COPY jenkins.sh /usr/local/bin/jenkins.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

# from a derived Dockerfile, can use `RUN plugin.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh
