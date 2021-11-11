FROM anapsix/alpine-java:8u201b09_jdk_unlimited as build

WORKDIR /app
COPY . /app

RUN sh gradlew clean build

FROM java:8-jre-alpine

WORKDIR /app
COPY --from=build /app/build/libs/*.jar /app/

RUN crontab -l | { cat; echo "1 8 * * * java -jar /app/BilibiliTask-1.0.9-all.jar >> /var/log/bilibili_task.log 2>&1"; } | crontab - \
    && touch /var/log/bilibili_task.log

CMD crond && tail -f /var/log/bilibili_task.log
