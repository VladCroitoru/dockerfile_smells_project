FROM ubuntu:trusty

MAINTAINER Krzysztof Pająk <kpajak@gmail.com>

# Env
ENV GERRIT_WAR /tmp/gerrit.war
ENV GERRIT_HOME /gerrit_home
ENV GERRIT_CONFIG_FILE ${GERRIT_HOME}/etc/gerrit.config
ENV BOOT_SEQUENCE_FILE /root/boot.sh
ENV GERRIT_VERSION 2.8.5

# Create user
#RUN useradd -m ${GERRIT_USER}

# Git, Java, Vim, curl installation
RUN apt-get update && apt-get install -y git openjdk-7-jre vim curl && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

# Gerrit download
ADD http://gerrit-releases.storage.googleapis.com/gerrit-${GERRIT_VERSION}.war ${GERRIT_WAR}

# Install Gerrit
RUN java -jar $GERRIT_WAR init --batch -d ${GERRIT_HOME}

# Push Gerrit config
ADD gerrit.config ${GERRIT_CONFIG_FILE}

# Push boot sequence
ADD boot.sh ${BOOT_SEQUENCE_FILE}

EXPOSE 8080 29418

# Default boot sequence
CMD ["/root/boot.sh"]
