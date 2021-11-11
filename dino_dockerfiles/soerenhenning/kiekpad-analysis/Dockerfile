FROM maven:3-jdk-8-onbuild
MAINTAINER SoerenHenning

RUN mv -f target/kiekpad-analysis.jar kiekpad-analysis.jar

VOLUME /usr/src/app/config

EXPOSE 10133 10134

CMD ["java", "-jar", "kiekpad-analysis.jar"]