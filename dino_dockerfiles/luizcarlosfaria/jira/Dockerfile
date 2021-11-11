FROM openjdk:8

ENV ATLASSIAN_HOME  			/opt/atlassian
ENV JIRA_INSTALL    			/opt/atlassian/jira
ENV JIRA_HOME     				/var/atlassian/application-data/jira
ENV JIRA_EXPORT                 /var/atlassian/application-data/jira/export
ENV JIRA_VERSION  				8.8.0
ENV TIME_ZONE 					America/Sao_Paulo
ENV MYSQL_CONNECTOR_VERSION		5.1.46

ADD ./mysql-connector-java-${MYSQL_CONNECTOR_VERSION}.tar.gz ${ATLASSIAN_HOME}/

ADD https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-${JIRA_VERSION}.tar.gz ${ATLASSIAN_HOME}/

RUN tar -xzf ${ATLASSIAN_HOME}/atlassian-jira-software-${JIRA_VERSION}.tar.gz -C ${ATLASSIAN_HOME}/ \
#&&  tar -xzf ${ATLASSIAN_HOME}/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}.tar.gz -C ${ATLASSIAN_HOME}/ \
&&  mv ${ATLASSIAN_HOME}/atlassian-jira-software-${JIRA_VERSION}-standalone ${JIRA_INSTALL} \
&&  mv ${ATLASSIAN_HOME}/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar ${JIRA_INSTALL}/lib/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar \
&&  chmod -R u=rwx,go-rwx ${JIRA_INSTALL} \
&&  mkdir -p ${JIRA_HOME} \
&&  chmod -R u=rwx,go-rwx ${JIRA_HOME} \
&&  echo "jira.home = ${JIRA_HOME}" > ${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties \
&&  cat ${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties \
&&  sed --in-place "s/java version/openjdk version/g" "${JIRA_INSTALL}/bin/check-java.sh" \
&&  echo "${TIME_ZONE}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata \
&& rm ${ATLASSIAN_HOME}/atlassian-jira-software-${JIRA_VERSION}.tar.gz \
&& rm -r ${ATLASSIAN_HOME}/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}/ 

EXPOSE 8080 8005
VOLUME ["${JIRA_HOME}"]
WORKDIR ${JIRA_INSTALL}/bin
ENTRYPOINT ["./start-jira.sh", "-fg"]