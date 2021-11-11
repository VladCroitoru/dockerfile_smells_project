FROM java:8
VOLUME /tmp
EXPOSE 1111
ADD /target/eurekaserver-1.0.jar /tmp/eurekaserver.jar
ENTRYPOINT ["java","-jar","/tmp/eurekaserver.jar"]