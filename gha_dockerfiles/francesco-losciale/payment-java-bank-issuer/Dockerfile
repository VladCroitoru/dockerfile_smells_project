FROM adoptopenjdk:11-jre-hotspot
RUN mkdir /opt/app
COPY build/libs/bank-issuer.jar /opt/app
EXPOSE 8080
CMD ["java", "-jar", "/opt/app/bank-issuer.jar"]