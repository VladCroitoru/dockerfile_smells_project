FROM tomcat:8.0-jre8
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

EXPOSE 8080


#
# env
#
ENV CATALINA_HOME=/usr/local/tomcat
ENV PATH=$PATH:$CATALINA_HOME/bin
RUN export CATALINA_HOME PATH

# tag:JDBC
ADD "$PWD"/lib/*.jar $CATALINA_HOME/lib/

# tag:MySQL
ADD "$PWD"/bin/catalina.sh_mysql $CATALINA_HOME/bin/catalina.sh

# tag:MySQL_workbook
ADD "$PWD"/conf/server.xml_workbook $CATALINA_HOME/conf/server.xml

# tag:MySQL_workbook
ADD "$PWD"/conf/context.xml_workbook $CATALINA_HOME/conf/context.xml

# tag:deploy_jaxrs-sample
#ADD "$PWD"/webapps/*.war $CATALINA_HOME/webapps/

# tag:bugfix
RUN chmod 755 /usr/local/tomcat/bin/catalina.sh
