FROM openjdk:8u102-jre
MAINTAINER H.-C.Guersoy <hcguersoy@gmail.com>
ADD https://www.dropbox.com/s/tdssjxrvqo8vg29/elasticshakespeare-0.0.2-SNAPSHOT.jar?dl=1 /elasticshakespeare.jar

EXPOSE 8080
EXPOSE 9200
EXPOSE 9300
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/elasticshakespeare.jar"]  