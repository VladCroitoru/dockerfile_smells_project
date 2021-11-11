FROM openjdk:8

ENV JIRA_HOME     /var/atlassian/application-data/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JIRA_VERSION  7.3.6

RUN set -x \
&& apt-get update --quiet \
&& apt-get install --quiet --yes --no-install-recommends -t jessie-backports libtcnative-1 \
&& apt-get install -y --quiet \
&& apt-get install -y wget --quiet \
&& apt-get clean \
&& mkdir -p "${JIRA_HOME}" \
&& mkdir -p "${JIRA_HOME}/caches/indexes" \
&& chmod -R 700 "${JIRA_HOME}" \
&& mkdir -p "${JIRA_INSTALL}/conf/Catalina" \
&& curl -Ls "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-core-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar" \
&& sed --in-place "s/java version/openjdk version/g" "${JIRA_INSTALL}/bin/check-java.sh" \
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties" \
&& touch -d "@0" "${JIRA_INSTALL}/conf/server.xml"
    
VOLUME ["/var/atlassian/application-data/jira", "/opt/atlassian/jira/logs"]
WORKDIR /opt/atlassian/jira

ADD build/server.xml /opt/atlassian/jira/conf

COPY "docker-entrypoint.sh" "/"
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8082

#CMD ["/sbin/my_init"]



RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

RUN apt-get purge mysql*
RUN apt-get autoremove
RUN apt-get autoclean
RUN rm -rf /etc/mysql/ /var/lib/mysql
RUN wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
RUN dpkg -i mysql-apt-config_0.6.0-1_all.deb || true


RUN apt-get update

RUN apt-get install -y mysql-server
#RUN rm -rf /var/lib/mysql/*

ADD build/my.cnf /etc/mysql/my.cnf
ADD build/dbconfig.xml /var/atlassian/application-data/jira

RUN mkdir /etc/mysql/run
ADD runit/mysql.sh /etc/mysql/run
RUN chmod +x /etc/mysql/run

ADD build/Setup /root/setup

ADD my_init.d/99_mysql_setup.sh /etc/my_init.d/99_mysql_setup.sh
RUN chmod +x /etc/my_init.d/99_mysql_setup.sh
ADD my_init.d/Jiradb.sql /etc/Jiradb.sql
RUN chmod +x /etc/Jiradb.sql

RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \
  sleep 5 && \
  /opt/atlassian/jira/bin/start-jira.sh && \
  service mysql start && \
  mysql -uroot -proot -e "CREATE DATABASE Jiradb" && \
  mysql -uroot -proot Jiradb < /etc/Jiradb.sql

#CMD docker exec -it mysql -uroot -proot Jiradb < /etc/Jiradb.sql


EXPOSE 3306

#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CMD ["/usr/bin/mysqld_safe"]
#CMD ["/opt/atlassian/jira/bin/start-jira.sh", "run"]
