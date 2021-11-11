FROM openjdk:8-jre-alpine
RUN mkdir /SpringBootSampleApp-jsp
COPY ./SpringBootSampleApp-jsp/SpringBootSampleWebApp-0.0.1-SNAPSHOT.war /SpringBootSampleApp-jsp/SpringBootSampleWebApp.war
WORKDIR /SpringBootSampleApp-jsp
EXPOSE 8181
CMD ["java", "-jar", "SpringBootSampleWebApp.war"]