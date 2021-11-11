FROM ubuntu:trusty

RUN apt-get update

RUN apt-get install -y curl openssl && apt-get clean
RUN apt-get install -y openjdk-7-jdk maven tomcat7 && apt-get clean

ADD . /tmp/uaa
WORKDIR /tmp/uaa/uaa
RUN mvn install
RUN rm -rf /var/lib/tomcat7/webapps/*
RUN cp /tmp/uaa/uaa/target/cloudfoundry-identity-uaa-?.?.?.war /var/lib/tomcat7/webapps/ROOT.war

RUN echo "CLOUD_FOUNDRY_CONFIG_PATH=/etc/uaa" >> /etc/tomcat7/catalina.properties

CMD service tomcat7 start && tail -f /var/lib/tomcat7/logs/catalina.out

