FROM tomcat:7-jre8

RUN wget https://github.com/Wondersoft/olaper/releases/download/0.0.2/olaper.war -P /usr/local/tomcat/webapps && \
    wget https://github.com/Wondersoft/olaper/archive/0.0.2.zip -P /tmp && \
    unzip -d /tmp /tmp/0.0.2.zip && \
    mkdir -p /etc/olaper

COPY cubes.json /etc/olaper/cubes.json
COPY tables.json /etc/olaper/tables.json

RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-3.1.14.tar.gz -P /tmp && \
    tar -xf /tmp/mysql-connector-java-3.1.14.tar.gz -C /tmp && \
    cp /tmp/mysql-connector-java-3.1.14/mysql-connector-java-3.1.14-bin.jar /usr/local/tomcat/lib/

CMD ["catalina.sh", "run"]
