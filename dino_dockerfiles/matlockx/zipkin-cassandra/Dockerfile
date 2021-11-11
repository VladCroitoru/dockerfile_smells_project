FROM poklet/cassandra

MAINTAINER m.joehren@gmail.com

ADD install_schema.sh /root/
WORKDIR /root
RUN wget https://raw2.github.com/twitter/zipkin/master/zipkin-cassandra/src/schema/cassandra-schema.txt
RUN /root/install_schema.sh
