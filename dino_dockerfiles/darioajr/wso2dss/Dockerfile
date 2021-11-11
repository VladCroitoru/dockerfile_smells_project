#
# WSO2 DSS 3.5.1
#

FROM java:8
MAINTAINER Dario Alves Junior, darioajr@gmail.com

RUN wget -P /opt https://s3-us-west-2.amazonaws.com/wso2-stratos/wso2dss-3.5.1.zip && \
    apt-get update && \
    apt-get install -y zip && \
    apt-get clean && \
    unzip /opt/wso2dss-3.5.1.zip -d /opt && \
    rm /opt/wso2dss-3.5.1.zip && \
    wget -P /opt http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.42.tar.gz && \
    tar -xvzf /opt/mysql-connector-java-5.1.42.tar.gz -C /opt && \
    mv /opt/mysql-connector-java-5.1.42/mysql-connector-java-5.1.42-bin.jar /opt/wso2dss-3.5.1/repository/components/extensions/mysql-connector-java-5.1.42-bin.jar && \
    rm -rf /opt/mysql-connector-java-5.1.42 && \
    rm /opt/mysql-connector-java-5.1.42.tar.gz && \
    wget -P /opt/wso2dss-3.5.1/repository/components/extensions/ http://central.maven.org/maven2/com/github/noraui/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
EXPOSE 9443 9763
CMD ["/opt/wso2dss-3.5.1/bin/wso2server.sh"]
