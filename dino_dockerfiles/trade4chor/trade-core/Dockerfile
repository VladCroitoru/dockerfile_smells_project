FROM openjdk:8-jdk as builder

RUN rm /dev/random && ln -s /dev/urandom /dev/random

COPY . /opt/trade4chor/trade
WORKDIR /opt/trade4chor/trade
RUN ./gradlew build


FROM openjdk:8-jdk

LABEL maintainer "Michael Hahn <mhahn.dev@gmail.com>"

ENV DOCKERIZE_VERSION v0.6.1

ENV TRADE_VERSION 1.0-SNAPSHOT
ENV PATH ${PATH}:/usr/local/bin/trade/bin:${JAVA_HOME}/bin

ENV TRADE_URL http://127.0.0.1:8081/api
ENV HDTApps_URL http://127.0.0.1:8082
ENV LOG_LEVEL INFO
ENV PERSISTENCE_MODE FILE
ENV DATA_DIRECTORY /tradeData
ENV MONGO_DB_URL mongodb://127.0.0.1:27017

RUN rm /dev/random && ln -s /dev/urandom /dev/random \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Copy the TraDE binary
COPY --from=builder /opt/trade4chor/trade/build/distributions /opt/trade4chor/trade

# Unzip TraDE archive file from /build into /usr/local/bin/trade
RUN tar -xf /opt/trade4chor/trade/traDE-all-${TRADE_VERSION}.tar -C /opt/trade4chor/trade
RUN ln -s /opt/trade4chor/trade/traDE-all-${TRADE_VERSION} /usr/local/bin/trade
RUN chmod -R a+x /usr/local/bin/trade/bin/*

ADD docker/config.properties.tpl /usr/local/bin/trade/config.properties.tpl
ADD docker/logback.xml.tpl /usr/local/bin/trade/logback.xml.tpl

WORKDIR /usr/local/bin/trade

EXPOSE 8081

CMD dockerize -template /usr/local/bin/trade/config.properties.tpl:/usr/local/bin/trade/config/config.properties \
    -template /usr/local/bin/trade/logback.xml.tpl:/usr/local/bin/trade/config/logback.xml \
    traDE

#
# Build and run:
#
#   docker build -t trade4chor/trade-core .
# 
#   docker run --name trade-core -p 8081:8081 -d trade4chor/trade-core
#
# The container is running in the background and remains active until it is explicitly stopped by running:
# 
#   docker stop trade-core
#
# The middleware is by default configured to run with the local file system as persistence layer.
# Nevertheless, the complete middleware can be configured according to users' requirements and run time context
# through corresponding files located under 'config/'.
# To mount customized configuration files located on your host into a container, start a container with corresponding
# data volumes (one for the emitted logs and one for the customized configuration files) through the following command:
#
#   docker run --name trade-core -p 8081:8081 -d -v /abs_path_to_persistent_dir/logs:/opt/trade/logs -v /abs_path_to_persistent_dir/config:/opt/trade/config trade4chor/trade-core
#
# As an concrete example on a Windows host:
#   docker run --name trade-core -p 8081:8081 -d -v c:/trade-data/logs:/opt/trade/logs -v c:/trade-data/config:/opt/trade/config trade4chor/trade-core
# ... and on a Linux host:
#   docker run --name trade-core -p 8081:8081 -d -v /trade-data/logs:/opt/trade/logs -v /trade-data/config:/opt/trade/config trade4chor/trade-core
#
# Templates for all required configuration files can be downloaded from GitHub: https://github.com/traDE4chor/trade-core/tree/master/config.
# Please provide all files through the shared host directory in order to run the middleware correctly.
# Further details about mounting host directories as data volumes are provided here: https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-directory-as-a-data-volume
# Don't forget to restart/recreate the trade-core container after changing the configuration so that the changes are applied.
#
# As an alternative option, the persistence layer can be configured through the specified environment variables PERSISTENCE_MODE, DATA_DIRECTORY, MONGO_DB_URL.
# To configure and run both services, TraDE Middleware and MongoDB, a corresponding docker-compose.yml is provided as an example.
#

#
# Interactive access for debugging:
#
#   docker run --rm --name trade-core -p 8081:8081 -ti trade4chor/trade-core bash
#
# Inside the container, the TraDE Middleware has to be configured and started manually through "traDE". In order to be able to use
# the shell after the middleware is started, the following command allows running the middleware in the background:
#
#   nohup traDE &
#
