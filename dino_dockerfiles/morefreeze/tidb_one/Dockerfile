FROM ubuntu:14.04
MAINTAINER pingcap info@pingcap.com

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/jre
ENV HBASE_PATH /hbase-0.98.15-hadoop2
ENV GOPATH=/opt/work
ENV GOBIN=$GOPATH/bin
ENV PATH $PATH:/usr/local/go/bin:$GOBIN

# Install Java7
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    apt-get update && apt-get install -y oracle-java7-installer && \
    apt-get install -y git \
        maven \
        wget \
        make && \
    wget https://archive.apache.org/dist/hbase/0.98.15/hbase-0.98.15-hadoop2-bin.tar.gz && \
    tar -C / -xzf hbase-0.98.15-hadoop2-bin.tar.gz && \
    git clone https://github.com/pingcap/themis.git && \
    cd themis && \
    mvn clean install -DskipTests && \
    cd - && \
    cp themis/themis-coprocessor/target/themis-coprocessor-1.0-SNAPSHOT-jar-with-dependencies.jar $HBASE_PATH/lib/ && \
    wget https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.5.1.linux-amd64.tar.gz && \
    mkdir -p /opt/work && \
    git clone http://github.com/pingcap/tidb.git $GOPATH/src/github.com/pingcap/tidb && \
    cd $GOPATH/src/github.com/pingcap/tidb && \
    make && make server && \
    cp $GOPATH/src/github.com/pingcap/tidb/tidb-server/tidb-server $GOPATH/bin/ && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /tmp/* && \
    rm -rf go1.5.1.linux-amd64.tar.gz \
        golang.tar.gz \
        themis \
        hbase-0.98.15-hadoop2-bin.tar.gz \
        hbase-0.98.15-hadoop2/docs \
        #$GOPATH/src \
        $GOPATH/pkg \
        /var/cache/oracle-jdk7-installer/ \
        /var/lib/apt/lists/* \
        /usr/local/go && \
    cd /usr/lib/jvm/java-7-oracle/ && find -not -path "./jre*" -delete

# tidb, use mysql -h container_ip -P 4000 -u root connect it
EXPOSE 4000
# ZooKeeper
EXPOSE 2181

# HMaster
EXPOSE 60000

# HMaster Web
EXPOSE 60010

# RegionServer
EXPOSE 60020

# RegionServer Web
EXPOSE 60030

COPY start-all.sh .
COPY hbase-site.xml $HBASE_PATH/conf/

CMD ["./start-all.sh"]
