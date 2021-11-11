FROM jboss/wildfly:16.0.0.Final

LABEL author="Arthur Gregorio"
LABEL email="arthurshakal@gmail.com"
LABEL application="webBudget v3.0.1-RELEASE"

# default environment vars for wildfly
ENV WF_ADMIN_USER webbudget
ENV WF_ADMIN_PASS webbudget

# default environment vars for database
ENV DB_HOST postgres
ENV DB_PORT 5432
ENV DB_NAME webbudget
ENV DB_USER sa_webbudget
ENV DB_PASS sa_webbudget

# define the user to run commands below
USER root

# create the folder where postgres driver will be placed
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/org/postgresql/main

# copy postgres driver
COPY files/module.xml /opt/jboss/wildfly/modules/system/layers/base/org/postgresql/main
COPY files/postgresql-42.2.5.jar /opt/jboss/wildfly/modules/system/layers/base/org/postgresql/main/

# copy wildfly configuration
COPY files/standalone.xml /opt/jboss/wildfly/standalone/configuration/standalone.xml

# copy application war file to deploy folder
COPY files/web-budget-3.0.1-RELEASE.war /opt/jboss/wildfly/standalone/deployments

# add wildfly admin user
RUN /opt/jboss/wildfly/bin/add-user.sh ${WF_ADMIN_USER} ${WF_ADMIN_PASS} --silent

# expose https port for application and management
EXPOSE 8443 9993

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]