FROM vmware/photon:1.0

RUN tdnf --refresh -y install \
        curl \
        gzip \
        iputils \
        openjre \
        tar
RUN tdnf clean all

# Install kafka distro
ENV KAFKA_VER 2.0.1
ENV KAFKA_HOME /usr/local/lib/kafka

RUN curl -L http://apache.mirrors.pair.com/kafka/${KAFKA_VER}/kafka_2.11-${KAFKA_VER}.tgz \
   -o /tmp/kafka-${KAFKA_VER}.tgz

RUN mkdir ${KAFKA_HOME} && \
    tar xzvf /tmp/kafka-${KAFKA_VER}.tgz -C ${KAFKA_HOME} --strip-components=1 && \
    rm -rf /tmp/kafka-${KAFKA_VER}.tgz

# Add wrapper scripts for common commands
COPY links/kafka-topics /usr/local/bin/
COPY links/kafka-console-producer /usr/local/bin
COPY links/kafka-console-consumer /usr/local/bin
COPY links/zookeeper-shell /usr/local/bin

CMD ["/bin/bash"]
