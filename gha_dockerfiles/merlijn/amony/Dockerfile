FROM openjdk:11-jdk-slim

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends ffmpeg;

# create directories
RUN mkdir /usr/amony
RUN mkdir /usr/amony/certs
RUN mkdir /usr/amony/videos

# copy files
COPY ./web-client/build /usr/amony/web-client
COPY ./server/target/scala-2.13/amony.jar /usr/amony
COPY ./server/src/main/resources/prod/application.conf /usr/amony

WORKDIR /usr/amony
EXPOSE 80
ENV JAVA_TOOL_OPTIONS "-Dconfig.file=/usr/amony/application.conf"
ENTRYPOINT ["java", "-jar", "amony.jar"]
