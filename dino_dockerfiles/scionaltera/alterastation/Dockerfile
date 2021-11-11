FROM frolvlad/alpine-oraclejdk8:slim
MAINTAINER Peter Keeler <scion@tarentum.org>
EXPOSE 8080
COPY . /opt/build/
RUN mkdir -p /opt/app \
&& cd /opt/build \
&& apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& ./gradlew clean build \
&& cp -v build/libs/alterastation*.jar /opt/app/app.jar \
&& cd /opt/app \
&& rm -rf /tmp/* /var/cache/apk/* /opt/build ~/.m2 ~/.gradle
CMD ["/usr/bin/java","-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005","-jar","/opt/app/app.jar"]