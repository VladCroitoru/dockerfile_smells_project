FROM folioci/alpine-jre-openjdk11:latest
MAINTAINER Ian.Ibbotson@k-int.com
VOLUME /tmp
ENV VERTICLE_FILE mod-rs.war
ENV VERTICLE_HOME /
COPY service/build/libs/mod-rs-*.*.*.jar mod-rs.war
EXPOSE 8080/tcp
# See https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-external-config
#     https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-external-config-relaxed-binding-from-environment-variables
# CMD java -Djava.security.egd=file:/dev/./urandom -Xshareclasses -Xscmx50M -Xtune:virtualized -jar /mod-rs.war
