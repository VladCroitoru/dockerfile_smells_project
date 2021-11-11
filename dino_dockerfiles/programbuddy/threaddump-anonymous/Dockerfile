FROM maven:3.3.9-jdk-8

MAINTAINER programbuddy <info@programbuddy.com>

RUN wget https://github.com/programbuddy/threaddump-anonymous/archive/master.zip && \
    unzip master.zip && \
    rm master.zip && \
    cd threaddump-anonymous-master && \
    mvn clean install

WORKDIR /threaddump-anonymous-master/target

CMD ["java", "-jar", "threaddump.anonymous-1.0-SNAPSHOT.jar", "out_anonymous_map.txt"]
