# Pull base image.
FROM ubuntu:14.04

ENV ES_PKG_NAME elasticsearch-1.5.0
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C
ENV ES_HEAP_SIZE 1g
ENV LANG C.UTF-8

# Setting ulimit values
ADD setUlimit.sh /

RUN \
    cd / && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get update && \
    apt-get install -yyq software-properties-common python-software-properties && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -qyy --no-install-recommends oracle-java8-installer oracle-java8-set-default && \
    wget https://download.elastic.co/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
    tar xvzf $ES_PKG_NAME.tar.gz && \
    mv /$ES_PKG_NAME /es && \
    ./es/bin/plugin --install elasticsearch/elasticsearch-mapper-attachments/2.5.0 && \
    ./es/bin/plugin --install elasticsearch/marvel/latest && \
    ./es/bin/plugin --install mobz/elasticsearch-head && \
    ./es/bin/plugin --install elasticsearch/elasticsearch-cloud-aws/2.5.1 && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer && \
    rm -f $ES_PKG_NAME.tar.gz /elasticsearch/config/elasticsearch.yml && \
    chmod 777 /setUlimit.sh

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Define mountable directories.
VOLUME ["/data"]

#COPY $configpath/config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
WORKDIR /data

# Define default command.
#CMD ["/es/bin/elasticsearch"]
CMD ["/setUlimit.sh"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300