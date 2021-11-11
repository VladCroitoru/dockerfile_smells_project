FROM kurron/docker-oracle-jdk-8:jdk1.8.0_72

MAINTAINER Ron Kurr <kurr@kurron.org>

ENV DEBIAN_FRONTEND noninteractive

# Install Ansible
RUN apt-get --quiet update && \
    apt-get --quiet --yes install python-setuptools python-dev unzip && \
    apt-get clean && \
    easy_install pip && \
    pip install ansible 

ADD https://services.gradle.org/distributions/gradle-2.10-bin.zip /tmp/gradle.zip

RUN mkdir -p /opt && \
    unzip /tmp/gradle.zip -d /opt && \
    rm /tmp/gradle.zip

ENV GRADLE_HOME /opt/gradle-2.10

LABEL org.kurron.ansible.version="latest-from-pip"
LABEL org.kurron.gradle.version="2.10"

VOLUME ["/home"]
VOLUME ["/pwd"]
WORKDIR /pwd

ENTRYPOINT ["/opt/gradle-2.10/bin/gradle"]
