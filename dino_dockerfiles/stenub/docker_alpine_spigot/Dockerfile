FROM anapsix/alpine-java:latest
MAINTAINER stenub v1.0

WORKDIR /builddir

RUN apk --no-cache add git wget && \
    wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar && \
    java -jar BuildTools.jar --rev 1.13.1 && \
    mkdir /spigot && \
    cp /builddir/spigot-*.jar /spigot && \
    rm -rf /builddir \
           /root/.gitconfig \
           /root/.m2 \
           /root/.oracle_jre_usage && \
    apk del git wget && \
    echo 'eula=true' > /spigot/eula.txt

WORKDIR /spigot

VOLUME /spigot

EXPOSE 25565

CMD java -Xms512M -Xmx1G -XX:+UseConcMarkSweepGC -jar spigot-*.jar

#CMD /bin/sh
