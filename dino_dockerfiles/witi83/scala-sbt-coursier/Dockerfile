#
# Scala sbt-coursier launcher Dockerfile (alpine)
#
# https://github.com/witi83/scala-sbt-coursier
#

FROM openjdk:8-alpine

ENV COURSIER_VERSION 1.0.0-RC6

VOLUME ["/home/user/app"]

RUN addgroup user && adduser -G user -D user && \
    apk update && apk add openssl && \
    cd /home/user && \
    mkdir -p ~/.sbt/0.13/plugins && \
    echo 'addSbtPlugin("io.get-coursier" % "sbt-coursier" % "1.0.0-RC6")' > ~/.sbt/0.13/plugins/build.sbt && \
    wget -q https://github.com/coursier/coursier/raw/v$COURSIER_VERSION/csbt && \
    chown -R user:user /home/user

USER user

WORKDIR /home/user/app

ENTRYPOINT ["sh", "../csbt"]
CMD ["run"]
