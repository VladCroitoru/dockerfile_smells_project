# use the openjdk base image
# TODO: use alpine?
FROM openjdk:8-jdk

ENV SBT_VERSION 0.13.15

# install SBT
RUN set -x && \
    apt-get update && \
    apt-get install -y apt-transport-https && \
    echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
    apt-get update && \
    apt-get install -y sbt=$SBT_VERSION && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sh"]