FROM qnib/u-terminal

ENV JAVA_HOME=/usr/ \
    JMX_VER=253
RUN apt-get update && \
    apt-get install -y openjdk-7-jdk maven git
RUN curl -sLo /tmp/jmxtrans-${JMX_VER}.deb http://central.maven.org/maven2/org/jmxtrans/jmxtrans/${JMX_VER}/jmxtrans-${JMX_VER}.deb && \
    dpkg -i /tmp/jmxtrans-${JMX_VER}.deb && \
    rm -f /tmp/jmxtrans-${JMX_VER}.deb
## Samza
RUN git clone http://git-wip-us.apache.org/repos/asf/samza.git /opt/samza && \
    cd /opt/samza && \
    ./gradlew  publishToMavenLocal
RUN git clone https://git.apache.org/samza-hello-samza.git /opt/hello-samza && \
    cd /opt/hello-samza && \
    ./bin/grid bootstrap && \
    mvn clean package
ADD etc/supervisord.d/kafka.ini \
    etc/supervisord.d/yarn-nodemanager.ini \
    etc/supervisord.d/yarn-resourcemanager.ini \
    etc/supervisord.d/zookeeper.ini \
    /etc/supervisord.d/
RUN mkdir -p /opt/hello-samza/deploy/samza/ && \
    tar xf /opt/hello-samza/target/hello-samza-0.10.0-dist.tar.gz -C /opt/hello-samza/deploy/samza/
WORKDIR /opt/hello-samza/
RUN echo "./deploy/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --max-messages 5 --topic wikipedia-raw" >> /root/.bash_history && \
    echo "./deploy/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --max-messages 5 --topic wikipedia-edits" >> /root/.bash_history && \
    echo "./deploy/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --max-messages 5 --topic wikipedia-stats" >> /root/.bash_history && \
    echo "./deploy/samza/bin/run-job.sh --config-factory=org.apache.samza.config.factories.PropertiesConfigFactory --config-path=file://$PWD/deploy/samza/config/wikipedia-stats.properties" >> /root/.bash_history && \
    echo "./deploy/samza/bin/run-job.sh --config-factory=org.apache.samza.config.factories.PropertiesConfigFactory --config-path=file://$PWD/deploy/samza/config/wikipedia-parser.properties" >> /root/.bash_history && \
    echo "./deploy/samza/bin/run-job.sh --config-factory=org.apache.samza.config.factories.PropertiesConfigFactory --config-path=file://$PWD/deploy/samza/config/wikipedia-feed.properties" >> /root/.bash_history
ADD etc/consul.d/hdfs.json \
    etc/consul.d/kafka.json	\
    etc/consul.d/sshd.json \
    etc/consul.d/yarn.json \
    etc/consul.d/zookeeper.json \
    etc/supervisord.d/jmxtrans.ini \
    /etc/consul.d/
ADD opt/qnib/jmxtrans/bin/start.sh /opt/qnib/jmxtrans/bin/
ADD opt/qnib/kafka/bin/check_kafka.sh /opt/qnib/kafka/bin/
ADD opt/qnib/zookeeper/bin/check.sh /opt/qnib/zookeeper/bin/
ADD root/id_rsa \
    root/id_rsa.pub \
    /root/.ssh/
RUN apt-get install -y netcat openssh-server && \
    mkdir -p /var/run/sshd
####### Highly unsecure... !1!! ###########
RUN echo "        StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    echo "        UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config && \
    echo "        AddressFamily inet" >> /etc/ssh/ssh_config
ADD etc/supervisord.d/sshd.ini /etc/supervisord.d/
ADD etc/supervisord.d/sshd.ini /etc/supervisord.d/
RUN rm -f /etc/consul.d/hdfs.json && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
RUN sed -i'' -e 's/localhost:2181/zookeeper.service.consul:2181/' /opt/hello-samza/deploy/samza/config/wikipedia-feed.properties && \
    sed -i'' -e 's/localhost:9092/kafka.service.consul:9092/' /opt/hello-samza/deploy/samza/config/wikipedia-feed.properties && \
    sed -i'' -e 's/localhost:2181/zookeeper.service.consul:2181/' /opt/hello-samza/deploy/samza/config/wikipedia-parser.properties && \
    sed -i'' -e 's/localhost:9092/kafka.service.consul:9092/' /opt/hello-samza/deploy/samza/config/wikipedia-parser.properties && \
    sed -i'' -e 's/localhost:2181/zookeeper.service.consul:2181/' /opt/hello-samza/deploy/samza/config/wikipedia-stats.properties && \
    sed -i'' -e 's/localhost:9092/kafka.service.consul:9092/' /opt/hello-samza/deploy/samza/config/wikipedia-stats.properties
ADD opt/qnib/kafka/bin/kafka-server-start.sh /opt/qnib/kafka/bin/
