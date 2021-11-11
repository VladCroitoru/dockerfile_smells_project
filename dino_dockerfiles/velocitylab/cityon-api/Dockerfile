FROM frolvlad/alpine-oraclejdk8:slim

## Install Application ################################

ADD build/libs/cityon-api.jar app.jar
RUN sh -c 'touch /app.jar'
RUN addgroup -S -g 1000 app
RUN adduser -S -u 1000 -G app app

EXPOSE 8080
VOLUME /mnt/logs

## Run container ###############################################

CMD [ "java -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]