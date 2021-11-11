FROM adoptopenjdk:11-jre-hotspot
RUN mkdir /opt/app
COPY build/libs/card-scheme.jar /opt/app
CMD ["java", "-jar", "/opt/app/card-scheme.jar"]