# download java 8 image 
FROM openjdk:8-jre-alpine
# copy jar file to home directory
COPY /build/libs/expense-manager-0.0.1-SNAPSHOT.jar expense-manager-0.0.1-SNAPSHOT.jar
ENTRYPOINT [ "java", "-jar", "expense-manager-0.0.1-SNAPSHOT.jar" ]
# expose port 8080
EXPOSE 8080