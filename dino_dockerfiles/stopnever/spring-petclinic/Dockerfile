FROM tutum/tomcat
RUN rm -rf /tomcat/webapps/*
#install maven and git to build project
RUN apt-get update && apt-get install -y wget git-core maven
RUN mkdir /opt/aspectj && cd /opt/aspectj &&\
    wget -O aspectjweaver-1.8.2.jar http://search.maven.org/remotecontent?filepath=org/aspectj/aspectjweaver/1.8.2/aspectjweaver-1.8.2.jar

#ADD ./setenv.sh /tomcat/bin/setenv.sh
ENV CATALINA_OPTS="$CATALINA_OPTS -javaagent:/opt/aspectj/aspectjweaver-1.8.2.jar"

# Pull petclinic
RUN git clone https://github.com/stopnever/spring-petclinic.git

# Build petclinic
WORKDIR /spring-petclinic
#RUN rm src/main/resources/stagemonitor.properties

#ADD ./stagemonitor.properties /spring-petclinic/src/main/resources/stagemonitor.properties

RUN mvn -Dmaven.test.skip=true package &&\
    mv /spring-petclinic/target/petclinic.war /tomcat/webapps/petclinic.war &&\
rm -rf /spring-petclinic
