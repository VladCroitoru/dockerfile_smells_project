FROM openjdk:11

ADD ./docker-entrypoint.sh /docker-entrypoint.sh
ADD ./build/libs/*.jar /aggregate-service/aggregate-service.jar

ENTRYPOINT [ "/bin/bash", "-c", "./docker-entrypoint.sh /aggregate-service/aggregate-service.jar" ]
