FROM centos:7

RUN yum install -y java-1.8.0-openjdk maven

RUN mkdir -p /opt/exhibitor
COPY settings.xml /opt/exhibitor/settings.xml
ADD https://raw.github.com/Netflix/exhibitor/master/exhibitor-standalone/src/main/resources/buildscripts/standalone/maven/pom.xml /opt/exhibitor/pom.xml
RUN mvn -f /opt/exhibitor/pom.xml -s /opt/exhibitor/settings.xml package
RUN mv /opt/exhibitor/target/exhibitor*.jar /opt/exhibitor/exhibitor.jar
COPY defaults.conf.template /opt/exhibitor/defaults.conf.template

ADD http://www.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz /opt/
RUN tar xvzf /opt/zookeeper-3.4.6.tar.gz -C /opt
RUN rm -f /opt/zookeeper-3.4.6.tar.gz
RUN mv /opt/zookeeper-* /opt/zookeeper

ADD run.sh /run.sh

EXPOSE 2181 2888 3888 8081

WORKDIR /opt/exhibitor

ENTRYPOINT ["/run.sh"]
