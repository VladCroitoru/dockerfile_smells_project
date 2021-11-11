FROM gradle
WORKDIR /home/gradle/spring-boot-admin
ADD build.gradle /home/gradle/spring-boot-admin
ADD src /home/gradle/spring-boot-admin/src
RUN gradle build

FROM openjdk
VOLUME /tmp
COPY --from=0 /home/gradle/spring-boot-admin/build/libs/*.jar app.jar
RUN bash -c 'touch /app.jar'
EXPOSE 8123
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
