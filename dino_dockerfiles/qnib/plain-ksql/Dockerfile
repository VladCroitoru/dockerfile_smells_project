FROM qnib/alpn-maven@sha256:f00ffb6462513fcd2fd0885efc8f6c0220bce5280cd4faa3301b9a5c297f6a3a AS build

ARG KSQL_SUB_VER=-pre10
ARG KSQL_BASE_VER=0.1
ARG CONFLUENT_VERSION=v3.3.x
ARG CONFLUENT_COMMON_VER=3.3.x

RUN apk --no-cache add git \
 && mkdir -p /usr/src/ \
 && cd /usr/src/ \
 && git clone --branch ${CONFLUENT_COMMON_VER} https://github.com/confluentinc/common \
 && cd common \
 && mvn -Dmaven.test.skip=true clean install
RUN git clone https://github.com/confluentinc/ksql /opt/ksql \
 && cd /opt/ksql/build-tools \
 && mvn -DskipTests --quiet clean package install \
 && cd /opt/ksql \
 && mvn -DskipTests --quiet clean package install


FROM qnib/alplain-openjre8

ENV KAFKA_BROKERS=tasks.brokers:9092 \
    KSQL_APP_ID=ksql_test \
    ENTRYPOINTS_DIR=/opt/qnib/entry
COPY opt/qnib/entry/21-ksqlserver-properties.sh /opt/qnib/entry/
COPY opt/qnib/ksql/server.properties /opt/qnib/ksql/
COPY --from=build /opt/ksql /opt/ksql/
#COPY --from=build /opt/ksql/bin/* /usr/bin/
#COPY --from=build /opt/ksql/ksql-cli/target/ksql-cli-*-SNAPSHOT.jar \
#    /opt/ksql/ksql-cli/target/ksql-cli-*-SNAPSHOT-standalone.jar \
#    /usr/share/java/ksql-cli/
#COPY --from=build /opt/ksql/ksql-rest-app/target/ksql-rest-app-*.jar \
#    /usr/share/java/ksql-rest-app/
#COPY --from=build /opt/ksql/ksql-core/target/ksql-core-*-SNAPSHOT.jar \
#     /usr/share/java/ksql-core/

CMD ["/opt/ksql/bin/ksql-server-start", "/etc/ksql/server.properties"]
