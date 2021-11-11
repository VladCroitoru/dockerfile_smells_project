FROM registry.access.redhat.com/ubi8/ubi-minimal as builder

MAINTAINER Shubham <shubham@linux.com>

RUN microdnf install git zip unzip maven wget java-1.8.0-openjdk-devel &&\
    microdnf clean all

ENV JAVA_HOME /usr/lib/jvm/java-openjdk
ENV M2_DIR=/m2
ENV M2_REPO=${M2_DIR}/repository
ENV MAVEN_OPTS="-Dmaven.repo.local=${M2_REPO}"


# Clone Janusgraph from a particular version and create jar
RUN git clone https://github.com/awslabs/dynamodb-janusgraph-storage-backend.git --branch jg0.1.1-1.1.0 /opt/dynamodb/dynamodb-janusgraph-storage-backend/ &&\
    cd /opt/dynamodb/dynamodb-janusgraph-storage-backend &&\
    mvn clean install

# Modify few entries in the install-gremlin-server.sh file
RUN cd /opt/dynamodb/dynamodb-janusgraph-storage-backend/ &&\
    sed -i "\#gpg --verify src/test/resources/${JANUSGRAPH_VANILLA_SERVER_ZIP}#d" src/test/resources/install-gremlin-server.sh &&\
    sed -i 's#JANUSGRAPH_VANILLA_SERVER_ZIP=.*#JANUSGRAPH_VANILLA_SERVER_ZIP=/opt/dynamodb/dynamodb-janusgraph-storage-backend/server/janusgraph-0.1.1-hadoop2.zip#' src/test/resources/install-gremlin-server.sh &&\
    src/test/resources/install-gremlin-server.sh

WORKDIR /opt/dynamodb/

# Cleanup Directories
RUN mkdir -p ${M2_DIR}/root &&\
    rm -Rf ${M2_REPO}/ &&\
    rm -rf ~/.m2/repository &&\
    rm -rf ~/.groovy/grapes &&\
    mkdir -p ${M2_REPO}/org/slf4j/slf4j-api/1.7.21/ &&\
    curl -o ${M2_REPO}/org/slf4j/slf4j-api/1.7.21/slf4j-api-1.7.21.jar https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.21/slf4j-api-1.7.21.jar

ADD scripts/entrypoint.sh /bin/entrypoint.sh

RUN chmod +x /bin/entrypoint.sh &&\
    chgrp -R 0 /opt/dynamodb/ &&\
    chmod -R g+rw /opt/dynamodb/ &&\
    find /opt/dynamodb/ -type d -exec chmod g+x {} +

ADD scripts/entrypoint-local.sh /bin/entrypoint-local.sh
RUN chmod +x /bin/entrypoint-local.sh

##############################################################################
FROM registry.access.redhat.com/ubi8/ubi-minimal

MAINTAINER arajkuma@redhat.com

EXPOSE 8182 5000

ENV PYTHONDONTWRITEBYTECODE=1
# Install JRE
RUN microdnf install java-1.8.0-openjdk-headless findutils python3 &&\
    microdnf clean all &&\
    rm -fr /var/cache/lib/{dnf,rpm}

RUN pip3 --no-cache-dir install awscli

COPY scripts/config.yaml /metrics/
RUN curl -o /metrics/jmx_prometheus_javaagent.jar https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.14.0/jmx_prometheus_javaagent-0.14.0.jar

# Copy artifacts from builder image
COPY --from=builder /opt/dynamodb/dynamodb-janusgraph-storage-backend/server/dynamodb-janusgraph-storage-backend-1.1.0 /opt/dynamodb/dynamodb-janusgraph-storage-backend/server/dynamodb-janusgraph-storage-backend-1.1.0
COPY --from=builder /bin/entrypoint.sh /bin/
COPY scripts/post-hook.sh /bin/
COPY --from=builder /bin/entrypoint-local.sh /bin

# Define non root user
USER 185
WORKDIR /opt/dynamodb

ENTRYPOINT ["/bin/entrypoint.sh"]
