FROM ubuntu:xenial
ENV JENKINS_UID 1000
ENV JENKINS_HOME /var/lib/jenkins_home
ENV DEBIAN_FRONTEND noninteractive
ENV SWARM_CLIENT_VERSION 2.0
ENV SWARM_CLIENT swarm-client-${SWARM_CLIENT_VERSION}-jar-with-dependencies.jar

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ccache \
        ssh-client \
        locales \
        gettext \
        binutils-dev \
        libboost-all-dev \
        libcurl4-openssl-dev \
        libexpat1-dev \
        libiberty-dev \
        libicu-dev \
        libncurses5-dev \
        libreadline-dev \
        zlib1g-dev \
        tcl-dev \
        python-dev \
        git \
        openjdk-8-jre \
        wget \
        fakeroot \
        xsltproc \
        docbook \
        docbook-xml \
        docbook-xsl \
        unzip && \
    apt-get clean
COPY startup.sh /usr/bin/startup.sh
ENTRYPOINT ["/usr/bin/startup.sh"]
COPY setup-slave.sh /tmp/setup-slave.sh
# now that all dependencies are complete setup the slave
RUN /bin/sh /tmp/setup-slave.sh && rm -f /tmp/setup-slave.sh
ADD http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/$SWARM_CLIENT_VERSION/$SWARM_CLIENT $JENKINS_HOME/
USER jenkins_slave
CMD []
