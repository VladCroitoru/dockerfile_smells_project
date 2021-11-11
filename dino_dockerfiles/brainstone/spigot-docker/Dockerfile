# ----------------------------------
# Spigot-Docker Dockerfile
# All Minecraft versions are prebuilt.
# ----------------------------------
FROM frolvlad/alpine-oraclejdk8:cleaned

MAINTAINER BrainStone

RUN apk update && \
    apk add bash curl git perl && \
    curl -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar; \
    for MC_VERSION in $( \
      curl -s https://hub.spigotmc.org/versions/ | \
      perl -nle 'print $& if m{(?<=")\d+\.\d+(?:\.\d+)?(?=\.json")}' | \
      sort -ut. -k 1,1nr -k 2,2nr -k 3,3nr \
    );  \
    do \
      java -jar BuildTools.jar --rev $MC_VERSION; \
    done && \
    rm -rf BuildTools.log.txt work
