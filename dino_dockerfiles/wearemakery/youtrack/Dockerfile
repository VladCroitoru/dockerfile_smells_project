FROM azul/zulu-openjdk-alpine:8u131

MAINTAINER Gyula Voros <gyulavoros87@gmail.com>

ENV YOUTRACK_VERSION 2017.3.35488

WORKDIR /opt/youtrack

RUN apk add --no-cache wget ca-certificates && \
    wget -q https://download-cf.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar && \
    mv youtrack-$YOUTRACK_VERSION.jar youtrack.jar && \
    apk del wget

EXPOSE 8080
VOLUME ["/root/teamsysdata", "/root/teamsysdata-backup"]

CMD ["sh", "-c", "java -Xmx1g -XX:MaxPermSize=250m -Djava.awt.headless=true -Djetbrains.youtrack.baseUrl=$BASE_URL -jar youtrack.jar 8080"]
