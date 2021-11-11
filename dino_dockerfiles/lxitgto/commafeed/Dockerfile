FROM lxitgto/docker-gitlab-runner-jdk-maven:jdk7

RUN mkdir /commafeed && mkdir /config && mkdir /data
WORKDIR /commafeed

ENV COMMAFEED_GIT https://github.com/Athou/commafeed.git
ENV COMMAFEED_VERSION 2.1.0

RUN git clone $COMMAFEED_GIT . && git checkout $COMMAFEED_VERSION && mvn clean package && cp /commafeed/config.dev.yml /config/config.yml

VOLUME /config
VOLUME /data

WORKDIR /data
ENTRYPOINT java -jar /commafeed/target/commafeed.jar server /config/config.yml
