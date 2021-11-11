FROM registry.access.redhat.com/ubi8/openjdk-11:latest as builder
COPY . /tmp/src
USER 0
# Since we want to execute the mvn command with RUN (and not when the container gets started),
# we have to do here some manual setup which would be made by the maven's entrypoint script
RUN mkdir -p /root/.m2 \
    && mkdir /root/.m2/repository \
EXPOSE 8080
VOLUME "${HOME}/.m2:/root/.m2"
VOLUME /tmp/
ARG API_DIR=NOTSET
WORKDIR ${API_DIR}
COPY infra/wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh

ARG SPRING_APPLICATION_JSON="{\"elasticsearch.service.url\":\"elasticsearch:9200\",\"elasticsearch.service.local.environment\":\"true\",\"elasticsearch.service.user\":\"elastic\",\"elasticsearch.service.password\":\"changeme\",\"mockbackend.url\":\"http:\/\/host.docker.internal:8182\",\"productmapping.url\":\"http:\/\/host.docker.internal:8187\",\"servicemapping.url\":\"http:\/\/host.docker.internal:8187\"}"
ENV SPRING_APPLICATION_JSON=$SPRING_APPLICATION_JSON
ENTRYPOINT ["./wait-for-it.sh", "elasticsearch:9200", "--strict", "--timeout=0", "--","mvn","spring-boot:run","-Drun.jvmArguments=\"-DSPRING_APPLICATION_JSON=${SPRING_APPLICATION_JSON} -DELASTICSEARCH_SERVICE_URL=${host.docker.internal}:9200\""]