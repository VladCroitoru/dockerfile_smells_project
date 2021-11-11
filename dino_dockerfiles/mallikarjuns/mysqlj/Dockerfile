FROM openjdk:8

ENV JIRA_HOME     /var/atlassian/application-data/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JIRA_VERSION  7.3.6

RUN set -x \
&& apt-get update --quiet \
&& apt-get install -y --quiet \
&& apt-get install -y wget --quiet \
&& apt-get clean \
&& mkdir -p "${JIRA_HOME}" \
&& mkdir -p "${JIRA_HOME}/caches/indexes" \
&& chmod -R 700 "${JIRA_HOME}" \
&& mkdir -p "${JIRA_INSTALL}/conf/Catalina" \
&& curl -Ls "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-core-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar" \

VOLUME ["/var/atlassian/application-data/jira", "/opt/atlassian/jira/logs"]
WORKDIR /opt/atlassian/jira

ADD build/server.xml /opt/atlassian/jira/conf

EXPOSE 8082


RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

RUN wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
RUN dpkg -i mysql-apt-config_0.6.0-1_all.deb


RUN apt-get update

RUN apt-get install -y mysql-server


ADD build/my.cnf /etc/mysql/my.cnf
ADD build/dbconfig.xml /var/atlassian/application-data/jira

ADD build/Setup /root/setup


ADD my_init.d/Jiradb.sql /etc/Jiradb.sql
RUN chmod +x /etc/Jiradb.sql

RUN /bin/bash -c /opt/atlassian/jira/bin/start-jira.sh && \
  service mysql start && \
  mysql -uroot -proot -e "CREATE DATABASE Jiradb" && \
  mysql -uroot -proot Jiradb < /etc/Jiradb.sql


EXPOSE 3306


