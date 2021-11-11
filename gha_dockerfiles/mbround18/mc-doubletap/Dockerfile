FROM gradle:jdk11@sha256:cc469186ac553a03be40cd95dee129357e2476573e4194e1285674f38dcfc3d1

RUN mkdir -p /data

COPY src build.gradle gradle.properties settings.gradle /data/
WORKDIR /data

RUN chmod 777 -R /data

CMD ["/usr/bin/gradle", "build"]