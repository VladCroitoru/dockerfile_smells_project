FROM ubuntu:trusty

ENV RIAK_VERSION 2.1.1-1

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get install -y oracle-java7-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk7-installer

RUN apt-get update && \
    apt-get install -y curl && \
    curl https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | bash && \
    apt-get install -y riak=${RIAK_VERSION} && \
    rm -rf /var/lib/apt/lists/*

ADD startup.sh /startup.sh

VOLUME /var/lib/riak
VOLUME /var/log/riak

EXPOSE 8087 8098

CMD ["/startup.sh"]
