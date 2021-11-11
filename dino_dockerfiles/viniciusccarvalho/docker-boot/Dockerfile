FROM java:7
VOLUME /tmp
ADD gs-spring-boot-docker-0.1.0.jar app.jar
EXPOSE 8080
RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-jar","/app.jar"]
