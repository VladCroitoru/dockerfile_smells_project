# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node.
FROM node:9-slim
MAINTAINER David Nussio <david.nussio@gmail.com>

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
RUN apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends \
    openssh-server software-properties-common build-essential git &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd

# Install Oracle Java 8
RUN  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list &&\
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list &&\
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&\
    apt-get update &&\
    apt-get install -y oracle-java8-installer

# Set java_home variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Set user jenkins to the image
RUN useradd -u 9000 -m -d /home/jenkins -s /bin/sh jenkins &&\
    echo "jenkins:jenkins" | chpasswd

RUN mkdir -p /home/jenkins/.m2/repository && \
    mkdir -p /data/jenkins/ && \
    chown -R jenkins:jenkins /home/jenkins /data/jenkins

RUN curl -0 -L http://npmjs.org/install.sh | sh

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
