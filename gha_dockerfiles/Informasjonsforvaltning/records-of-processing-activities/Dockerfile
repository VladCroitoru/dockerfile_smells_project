FROM openjdk:15-slim

ENV TZ=Europe/Oslo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

VOLUME /tmp
ADD /target/records-of-processing-activities.jar app.jar

CMD java -jar $JAVA_OPTS app.jar
