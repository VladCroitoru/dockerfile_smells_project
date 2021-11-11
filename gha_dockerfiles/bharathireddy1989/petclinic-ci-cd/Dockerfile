FROM maven:3.6.3-openjdk-11 AS maven
RUN apt-get update -y && apt-get upgrade -y && apt-get install git -y && apt-get install unzip -y
WORKDIR /opt
RUN wget https://mirrors.estointernet.in/apache/tomcat/tomcat-9/v9.0.48/bin/apache-tomcat-9.0.48.zip
RUN  unzip apache-tomcat-9.0.48.zip
RUN mv apache-tomcat-9.0.48 tomcat
RUN chmod -R 700 tomcat
WORKDIR /opt
RUN git clone https://github.com/bharathireddy1989/spring-framework-petclinic.git
WORKDIR /opt/spring-framework-petclinic
RUN mvn clean package
WORKDIR /opt/spring-framework-petclinic/target
RUN cp -R petclinic.war /opt/tomcat/webapps/
EXPOSE 8080
CMD chmod +x /opt/tomcat/bin/catalina.sh
CMD /opt/tomcat/bin/catalina.sh run
