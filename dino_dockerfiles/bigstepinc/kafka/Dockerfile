FROM mcristinagrosu/bigstepinc_java_8

RUN apk update 
RUN apk add --no-cache openssh wget tar bash curl unzip alpine-sdk

# Apache Kafka
RUN cd /opt && \
    wget http://apache.mirror.anlx.net/kafka/0.10.1.0/kafka_2.11-0.10.1.0.tgz 
    
RUN cd /opt && \
    tar xzvf /opt/kafka_2.11-0.10.1.0.tgz 
    
ENV KAFKA_HOME /opt/kafka_2.11-0.10.1.0 

RUN rm -rf /opt/kafka_2.11-0.10.1.0.tgz

# Install Kafka and Kafka Manager
ENV SBT_VERSION 0.13.11
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install sbt
RUN curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built

RUN cd /tmp && \
    curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built &&\
    git clone https://github.com/yahoo/kafka-manager.git && \
    cd kafka-manager && \
    sbt clean dist && \
    mv ./target/universal/kafka-manager*.zip /opt && \
    cd /opt && \
    unzip kafka-manager*.zip && \
    ln -s $(find kafka-manager* -type d -prune) kafka-manager
    
RUN rm /opt/kafka-manager*.zip

ENV KAFKA_MANAGER_HOME /opt/kafka-manager

ADD start-kafka-manager.sh /usr/bin/
ADD entrypoint.sh /opt/entrypoint.sh

RUN chmod 777 /opt/entrypoint.sh
RUN chmod 777 /usr/bin/start-kafka-manager.sh

RUN apk del wget tar curl unzip

#RUN /opt/entrypoint.sh

EXPOSE 2181 2888 3888 9092 9000

ENTRYPOINT ["/opt/entrypoint.sh"]
