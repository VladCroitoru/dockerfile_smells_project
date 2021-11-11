FROM wmarinho/pentaho-biserver:6.1

MAINTAINER Pablo González pablodgonzalez@gmail.com

RUN wget --progress=dot:giga http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.39.zip -O mysql-connector-java-5.1.39.zip; \
    unzip -qjn mysql-connector-java-5.1.39.zip mysql-connector-java-5.1.39/mysql-connector-java-5.1.39-bin.jar -d $PENTAHO_HOME/biserver-ce/tomcat/lib/; \
    rm -f mysql-connector-java-5.1.39.zip $PENTAHO_HOME/biserver-ce/tomcat/lib/mysql-connector-java-5.1.17.jar; \
    sed -i s/docbase/docBase/ biserver-ce/tomcat/webapps/pentaho/META-INF/context.xml

CMD ["sh", "scripts/run.sh"]