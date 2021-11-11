FROM openjdk:9-jre-slim
LABEL maintainer Jakub Pomykała <jakub.pomykala@gmail.com>
ENV PATH					$PATH:$JAVA_HOME/bin
ENV JAVA_OPTS				"-server -XX:+UseG1GC -XX:+UseStringDeduplication -XX:+OptimizeStringConcat -Dsun.net.inetaddr.ttl=60"
ENV HEAP_SPACE				"-Xms768m -Xmx1g"
ENV REMOTE_DEBUG			"-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1044"

ENV TIME_ZONE				Europe/Warsaw
ENV SPRING_BOOT_PROFILE		live

RUN echo "$TIME_ZONE" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

WORKDIR /app

EXPOSE 8080
EXPOSE 1044

COPY app.jar /app/app.jar

CMD ["/bin/sh", "-c", "java $HEAP_SPACE $JAVA_OPTS -jar /app/app.jar --spring.profiles.active=$SPRING_BOOT_PROFILE"]