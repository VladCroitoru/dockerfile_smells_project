FROM maven:3.6.3-openjdk-11 AS maven
RUN apt-get update -y && apt-get upgrade -y && apt-get install git -y && apt-get install unzip -y
WORKDIR /opt
RUN git clone https://github.com/bharathireddy1989/spring-framework-petclinic.git
WORKDIR /opt/spring-framework-petclinic
RUN mvn clean package
WORKDIR /opt/spring-framework-petclinic/target
EXPOSE 8080
