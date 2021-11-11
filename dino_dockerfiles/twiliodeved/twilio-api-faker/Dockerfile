FROM gradle:alpine

WORKDIR /project

COPY . /project

USER root

EXPOSE 443 

RUN gradle build

CMD ["java", "-jar", "/project/build/libs/project.jar"]
