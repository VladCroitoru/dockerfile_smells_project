############################################################
# Dockerfile to run Atlassian Bamboo
# Based on phusion/baseimage image
############################################################

FROM jjworren/docker-base:jessie

MAINTAINER JJWorren "jjworren@release.cz"

# Set environment 
ENV BAMBOO_VERSION 5.9.7
ENV BAMBOO_INSTALL /opt/atlassian/bamboo
ENV BAMBOO_HOME    /var/atlassian/bamboo

# Expose ports
EXPOSE 8085

# Update system
RUN apt-get update && apt-get upgrade --yes

# install wget for late use
RUN apt-get install --yes wget

# Install JDK 7 and VCS tools //thanks to hwuethrich/bamboo-server
RUN apt-get install -yq python-software-properties && add-apt-repository ppa:webupd8team/java -y && apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -yq oracle-java7-installer git subversion

# download and extract bamboo
RUN mkdir -p "${BAMBOO_INSTALL}" \
    && wget -qO- "https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz" | tar -xz --directory="${BAMBOO_INSTALL}" \
    && echo "set bamboo.home = ${BAMBOO_HOME}" > "${BAMBOO_INSTALL}/atlassian-bamboo-${BAMBOO_VERSION}/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties"

# Download and install mysql jdbc driver
RUN wget -qO- http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.34.tar.gz | tar -xz --directory="/tmp" "mysql-connector-java-5.1.34/mysql-connector-java-5.1.34-bin.jar"
RUN mv "/tmp/mysql-connector-java-5.1.34/mysql-connector-java-5.1.34-bin.jar" \
	"${BAMBOO_INSTALL}/atlassian-bamboo-${BAMBOO_VERSION}/atlassian-bamboo/WEB-INF/lib/"

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Dirs
VOLUME ["/var/atlassian/bamboo"]

ENTRYPOINT ${BAMBOO_INSTALL}/atlassian-bamboo-${BAMBOO_VERSION}/bin/start-bamboo.sh -fg
