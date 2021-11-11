FROM java:8-jdk
RUN mkdir -p /usr/app
COPY ./target/*.jar /usr/app
WORKDIR /usr/app
EXPOSE 5000
ENTRYPOINT ["java","-jar","SpringBootMavenExample-1.3.5.RELEASE.jar"]
