FROM    alpine:3.2
ENV     RDECK_BASE=/opt/rundeck
ENV     RDECK_JAR=$RDECK_BASE/app.jar
ENV     PATH=$PATH:$RDECK_BASE/tools/bin
RUN     apk add --update openjdk7-jre bash curl && \
        mkdir -p $RDECK_BASE && \
        wget -O $RDECK_JAR \
            http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.6.2.jar && \
        rm -Rf /var/cache/apk/*
COPY    run.sh /bin/rundeck
EXPOSE  4440
VOLUME  /opt/rundeck
CMD     rundeck
