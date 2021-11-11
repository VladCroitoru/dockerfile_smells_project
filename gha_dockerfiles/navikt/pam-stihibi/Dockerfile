FROM ghcr.io/graalvm/graalvm-ce:java11-21.2.0 AS graalvm
RUN gu install native-image
WORKDIR /home/app
COPY build/docker/layers/libs /home/app/libs
COPY build/docker/layers/resources /home/app/resources
COPY build/docker/layers/application.jar /home/app/application.jar
COPY build/generated/resources/graalvm /home/app/generated/resources/graalvm
RUN native-image -H:Class=no.nav.arbeidsplassen.stihibi.Application -H:Name=application --initialize-at-build-time=net.logstash -H:ResourceConfigurationFiles=generated/resources/graalvm/resource-config.json -R:PercentTimeInIncrementalCollection=75 -R:MaxHeapSize=256m  --no-fallback -cp /home/app/libs/*.jar:/home/app/resources:/home/app/application.jar
FROM frolvlad/alpine-glibc:alpine-3.12
RUN apk update && apk add libstdc++
COPY --from=graalvm /home/app/application /app/application
COPY scripts/run.sh /run.sh
ENTRYPOINT ["/run.sh"]
