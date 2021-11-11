FROM maven:3-jdk-8-onbuild
MAINTAINER SoerenHenning

RUN mv -f target/kiekpad-viz-provider.jar kiekpad-viz-provider.jar
RUN sh -c 'touch kiekpad-viz-provider.jar'

VOLUME /usr/src/app/config

EXPOSE 8080

CMD ["java", "-jar", "kiekpad-viz-provider.jar"]