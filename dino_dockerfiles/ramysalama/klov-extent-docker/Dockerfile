
FROM openjdk:8-jdk-alpine as java

ENV src_folder /sde/

COPY klov-0.1.0 $src_folder/klov-0.1.0

RUN chmod -R 755 $src_folder
WORKDIR $src_folder/klov-0.1.0

EXPOSE 80

CMD ["java","-jar","klov-0.1.0.jar"]
