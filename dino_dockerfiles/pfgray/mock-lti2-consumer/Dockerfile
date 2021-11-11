FROM maven:3.3.3-jdk-8

#build mock-rest
WORKDIR /root
COPY ./ /root/mock-lti2-consumer
WORKDIR /root/mock-lti2-consumer
RUN mvn clean install spring-boot:repackage

#run tomcat
WORKDIR /root/mock-lti2-consumer
EXPOSE 8080
CMD ["java", "-jar", "target/mock-lti2-consumer.jar"]
