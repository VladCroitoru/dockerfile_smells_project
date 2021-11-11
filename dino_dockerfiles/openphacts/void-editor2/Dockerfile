FROM tomcat:8-jre7
RUN rm -rf /usr/local/tomcat/webapps/ && mkdir /usr/local/tomcat/webapps/ /usr/local/src/voidEditor
WORKDIR /usr/local/src/voidEditor
COPY voidEditor/src /usr/local/src/voidEditor/src
COPY voidEditor/pom.xml /usr/local/src/voidEditor/pom.xml

RUN DEBIAN_FRONTEND="noninteractive" apt-get -q update &&\
 apt-get install -y --force-yes --no-install-recommends --auto-remove openjdk-7-jdk maven &&\
 mvn package -DskipTests &&\
 cp target/ROOT.war /usr/local/tomcat/webapps/ &&\
 mvn clean &&\
 rm -rf $HOME/.m2 &&\
 apt-get purge -y openjdk-7-jdk maven &&\
 apt-get autoremove -y --purge &&\
 apt-get -q clean &&\
 rm -rf /var/lib/apt/lists/* 


