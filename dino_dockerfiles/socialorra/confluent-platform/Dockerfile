FROM frolvlad/alpine-oraclejdk8

LABEL version="1.0"

RUN apk --update add unzip wget bash coreutils

# packed up into a single RUN (no ADD) command to save space inside the container
RUN wget http://packages.confluent.io/archive/2.0/confluent-2.0.0-2.11.7.zip && \
    unzip /confluent-2.0.0-2.11.7.zip -d / && \
		rm -f /confluent-2.0.0-2.11.7.zip
	
EXPOSE 9092 2181 8081 

COPY scripts/confluent-start.sh /

ENTRYPOINT ["/confluent-start.sh"]

VOLUME ["/kafka-logs", "/zookeeper", "/logs"]

