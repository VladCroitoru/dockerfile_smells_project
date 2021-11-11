FROM openjdk:8u121-jdk-alpine
LABEL maintainer "Gary A. Stafford <garystafford@rochester.rr.com>"
ENV REFRESHED_AT 2017-05-14
VOLUME /tmp
EXPOSE 8095
RUN set -ex \
  && apk update \
  && apk upgrade \
  && apk add git
RUN mkdir /election \
  && git clone --depth 1 --branch build-artifacts \
      "https://github.com/garystafford/election-service.git" /election \
  && cd /election \
  && mv election-service-*.jar election-service.jar
ENV JAVA_OPTS=""
CMD [ "java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "election/election-service.jar" ]
