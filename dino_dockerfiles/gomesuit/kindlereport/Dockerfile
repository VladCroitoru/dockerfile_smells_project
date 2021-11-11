FROM maven:3.3.9-jdk-8

EXPOSE 8080
ENV LANG en_US.UTF-8

# set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN mkdir /app
WORKDIR /app

# maven build
COPY pom.xml .
COPY src src
RUN mvn package -Prelease -Dmaven.test.skip=true

CMD java -jar \
    -Duser.timezone=Asia/Tokyo \
    -Dfile.encoding=UTF-8 \
    $JAVA_OPTS \
    /app/target/KindleReport-0.0.1-SNAPSHOT.jar

