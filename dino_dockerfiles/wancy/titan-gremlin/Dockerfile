FROM java:latest

LABEL Description="Titan Graph DB with Gremlin to be used with Cassandra and Elasticsearch" Version="1.0" Tags="cassandra,elasticsearch,graph,gremlin,titan"

WORKDIR /opt/titan-1.0.0-hadoop1

RUN curl -o /opt/titan.zip http://s3.thinkaurelius.com/downloads/titan/titan-1.0.0-hadoop1.zip

RUN unzip /opt/titan.zip -d /opt/ && \
    rm /opt/titan.zip

ADD configure.sh /opt/titan-1.0.0-hadoop1/
ADD run.sh /opt/titan-1.0.0-hadoop1/bin/
RUN chmod 744 /opt/titan-1.0.0-hadoop1/bin/run.sh

EXPOSE 8182

RUN sh configure.sh

ENTRYPOINT ["/opt/titan-1.0.0-hadoop1/bin/run.sh", "start"]
