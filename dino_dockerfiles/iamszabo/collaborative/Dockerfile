FROM java:8

ADD target/collaborative.jar /opt/collaborative/
EXPOSE 8080
WORKDIR /opt/collaborative/
CMD ["java", "-Xms512m", "-Xmx1g", "-jar", "collaborative.jar"]