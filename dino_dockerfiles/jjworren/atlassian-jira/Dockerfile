############################################################
# Dockerfile to run Atlassian Jira
# Based on phusion/baseimage image
############################################################

FROM jjworren/docker-base:jessie

MAINTAINER Jan Kubat "jan.kubat@release.cz"

# Set environment 
ENV JIRA_VERSION 7.0.5
ENV JIRA_INSTALL /opt/atlassian/jira
ENV JIRA_HOME    /var/atlassian/jira

# Expose ports
EXPOSE 8080

# Update system
RUN apt-get update && apt-get upgrade --yes

# install wget for late use
RUN apt-get install --yes wget

# Install JDK 7 and VCS tools //thanks to hwuethrich/bamboo-server
#RUN apt-get install -yq software-properties-common && add-apt-repository ppa:webupd8team/java -y && apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
#RUN apt-get install -yq oracle-java7-installer git subversion

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN apt-get update
RUN apt-get install -y oracle-java8-installer

# download and extract jira
RUN mkdir -p "${JIRA_INSTALL}"
RUN wget -qO- "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-7.0.0-jira-${JIRA_VERSION}.tar.gz" | tar -xz --directory="${JIRA_INSTALL}"
RUN mv "${JIRA_INSTALL}/atlassian-jira-software-${JIRA_VERSION}-standalone" "${JIRA_INSTALL}/atlassian-jira-${JIRA_VERSION}"
RUN echo "set jira.home = ${JIRA_HOME}" > "${JIRA_INSTALL}/atlassian-jira-${JIRA_VERSION}/atlassian-jira/WEB-INF/classes/jira-application.properties"

# Download and install mysql jdbc driver
RUN wget -qO- http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.34.tar.gz | tar -xz --directory="/tmp" "mysql-connector-java-5.1.34/mysql-connector-java-5.1.34-bin.jar"
RUN mv "/tmp/mysql-connector-java-5.1.34/mysql-connector-java-5.1.34-bin.jar" \
	"${JIRA_INSTALL}/atlassian-jira-${JIRA_VERSION}/atlassian-jira/WEB-INF/lib/"

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Dirs
VOLUME ["/var/atlassian/jira"]

# Start jira
ENTRYPOINT ${JIRA_INSTALL}/atlassian-jira-${JIRA_VERSION}/bin/start-jira.sh -fg
