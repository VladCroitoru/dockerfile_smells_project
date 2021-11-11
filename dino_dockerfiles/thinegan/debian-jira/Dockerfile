# Install Atlassian Jira in Debian Stretch (x64bit)
FROM debian:stretch
MAINTAINER Thinegan Ratnam <thinegan@thinegan.com>

# Environment Config
ENV JIRA_HOME       /home/www/public_html/jira-data.server.com
ENV JIRA_INSTALL    /home/www/public_html/jira-install.server.com
ENV JIRA_VERSION    7.5.1
ENV MYSQL_CON_JAVA  5.1.44
ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME       /usr/lib/jvm/java-8-oracle
ENV WORKDIR         /home/www/public_html
ENV JIRA_USER       jira
ENV JIRA_GROUP      jira

# Jira require prerequisites install
RUN \
  apt-get update && \
  apt-get install -y software-properties-common gnupg curl wget xmlstarlet

# Install Java.
RUN \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Copy Jira config - Unattended install mode
COPY response.varfile ${WORKDIR}/response.varfile

# Install Jira
RUN \
  mkdir -p ${JIRA_INSTALL} && \
  mkdir -p ${JIRA_HOME} && \
  cd ${WORKDIR} && \
  wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}-x64.bin && \
  chmod +x atlassian-jira-software-${JIRA_VERSION}-x64.bin && \
  /bin/bash atlassian-jira-software-${JIRA_VERSION}-x64.bin -q -varfile response.varfile

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /docker-entrypoint.sh

# Configure Jira Memory (Min 1GB RAM)
RUN \
  sed -i 's/384m/768m/g' ${JIRA_INSTALL}/bin/setenv.sh  && \
  sed -i 's/768m/1024m/g' ${JIRA_INSTALL}/bin/setenv.sh

# Install Mysql Connector Java
RUN \
  wget "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_CON_JAVA}.tar.gz" && \
  tar -zxf mysql-connector-java-${MYSQL_CON_JAVA}.tar.gz && \
  cp mysql-connector-java-${MYSQL_CON_JAVA}/mysql-connector-java-${MYSQL_CON_JAVA}-bin.jar ${JIRA_INSTALL}/lib/

# Install Run Jira symlink
RUN \
  ln -sf ${JIRA_INSTALL}/bin/start-jira.sh /usr/bin/jira && \
  chmod +x /usr/bin/jira

# Post Install & Cleanup
RUN \
  chmod +x -R ${JIRA_INSTALL} && \
  chmod +x -R ${JIRA_HOME} && \
  chown -R ${JIRA_USER}:${JIRA_GROUP} ${JIRA_INSTALL} && \
  chown -R ${JIRA_USER}:${JIRA_GROUP} ${JIRA_HOME} && \
  rm -rf ${WORKDIR}/atlassian-jira-software-${JIRA_VERSION}-x64.bin

# Define working directory.
WORKDIR ${JIRA_HOME}

# Startup
EXPOSE 8080

# Define default command.
CMD ["jira", "run"]
