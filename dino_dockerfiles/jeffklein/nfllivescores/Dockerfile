FROM anapsix/alpine-java:8_jdk
MAINTAINER Jeff Klein "jeff@jeffklein.org"

ENV PROJECT nfllivescores
ENV VERSION 0.1.0

# this is a hack to get around a DNS misconfiguration in alpine linux's base image
RUN sed -i -e 's/dl-cdn/dl-4/' /etc/apk/repositories && \
    apk add --no-cache \
        bash \
        git

WORKDIR /
RUN git clone https://github.com/jeffklein/$PROJECT.git && \
    cd $PROJECT && \
    chmod u+x ./gradlew && \
    ./gradlew build -x test

WORKDIR /$PROJECT/build/libs
EXPOSE 8080
CMD java -jar ./$PROJECT-springboot-$VERSION.jar
