FROM kawayu168/debian-kafka:stretch
#
#
#
MAINTAINER Haruki Yukawa

ENV APACHE_MIRROR=http://ftp.jaist.ac.jp
ENV KAFKA_VERSION=0.11.0.0
ENV KAFKA_BINARY_VERSION=kafka_2.11-$KAFKA_VERSION

ADD configure_s3_sink.sh /configure_s3_sink.sh

# download Kafka and build kafka-connect-s3
RUN wget "$APACHE_MIRROR/pub/apache/kafka/$KAFKA_VERSION/$KAFKA_BINARY_VERSION.tgz" -O /$KAFKA_BINARY_VERSION.tgz && \
    tar -zxf /$KAFKA_BINARY_VERSION.tgz && \
    rm /$KAFKA_BINARY_VERSION.tgz && \
    ln -s /$KAFKA_BINARY_VERSION kafka && \
    mkdir -p /tmp/sink && \
    git clone https://github.com/kawayu168/kafka-connect-s3.git /tmp/sink/kafka-connect-s3 && \
    cd /tmp/sink/kafka-connect-s3 && \
    mvn assembly:assembly -DdescriptorId=jar-with-dependencies && \
    mv /tmp/sink/kafka-connect-s3/target/kafka-connect-s3-0.0.3-jar-with-dependencies.jar /kafka/ && \
    mv /tmp/sink/kafka-connect-s3/connect-s3-sink.properties /kafka/ && \
    mv /tmp/sink/kafka-connect-s3/connect-worker.properties /kafka/ && \
    rm -rf /tmp/*

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/kafka/bin
ENV CLASSPATH=/kafka-connect-s3-0.0.3-jar-with-dependencies.jar

RUN chmod ugo+rx /configure_s3_sink.sh
CMD ["/configure_s3_sink.sh"]
