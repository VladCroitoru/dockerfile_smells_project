FROM java:8

# The Scala 2.11 build is currently recommended by the project.
ENV KAFKA_VERSION=0.10.1.1 KAFKA_SCALA_VERSION=2.11 JMX_PORT=7203
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN mkdir /kafka /data /logs

RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb
RUN dpkg -i dumb-init_*.deb

# Download Kafka binary distribution
ADD http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE} /tmp/
ADD https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.md5 /tmp/

WORKDIR /tmp

# Check artifact digest integrity
RUN echo VERIFY CHECKSUM: && \
  gpg --print-md MD5 ${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \
  cat ${KAFKA_RELEASE_ARCHIVE}.md5

# Install Kafka to /kafka
RUN tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \
  rm -rf kafka_*

ADD config /kafka/config
ADD start.sh /start.sh


ENV PATH /kafka/bin:$PATH
WORKDIR /kafka

# broker, jmx
EXPOSE 9092 ${JMX_PORT}
VOLUME [ "/data", "/logs" ]

ENTRYPOINT ["/usr/bin/dumb-init", "/start.sh"]
