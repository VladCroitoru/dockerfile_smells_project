FROM tomcat:8-jre8

# update packages and install maven 
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y vim wget curl git maven

RUN export DEBIAN_FRONTEND=noninteractive && apt-get install -y openjdk-8-jdk

RUN mkdir -p /local/git
WORKDIR /local/git
ADD src /local/git/src
ADD pom.xml /local/git/pom.xml

RUN mvn install
RUN cp /local/git/target/ComptesPerso.war /usr/local/tomcat/webapps/ROOT.war

ADD heroku/database.properties /tmp/database.properties

RUN /bin/rm -rf /usr/local/tomcat/webapps/ROOT

ENV ext.properties.dir=file:/tmp/
ENV JDBC_DATABASE_URL=jdbc:postgresql://database/postgres
ENV JDBC_DATABASE_USERNAME=postgres
ENV JDBC_DATABASE_PASSWORD=
