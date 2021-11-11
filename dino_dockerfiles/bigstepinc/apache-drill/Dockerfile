FROM java:openjdk-7-jre

RUN mkdir -p /drill-scripts && \
    mkdir -p /opt/drill && \
    mkdir -p /var/log/drill

RUN curl -o apache-drill-1.4.0.tar.gz http://www.eu.apache.org/dist/drill/drill-1.4.0/apache-drill-1.4.0.tar.gz && \
    tar -zxpf apache-drill-1.4.0.tar.gz -C /opt/drill
RUN rm apache-drill-1.4.0.tar.gz

#use DRILL_MAX_DIRECT_MEMORY and DRILL_HEAP to control the memory allocation
#also use  DRILL_CLUSTER and ZOOKEEPER

ADD drill-env.sh /opt/drill/apache-drill-1.4.0/conf/drill-env.sh

ENV DRILL_LOG_DIR=/var/log/drill
ENV DRILLBIT_LOG_PATH=/var/log/drill/drillbit.log
ENV DRILLBIT_QUERY_LOG_PATH=/var/log/drill/drill-query.log
ENV DRILL_MAX_DIRECT_MEMORY=8G
ENV DRILL_HEAP=4G  
ENV DRILL_CLUSTER=drillbit1

ENTRYPOINT /opt/drill/apache-drill-1.4.0/bin/runbit

EXPOSE 8047
