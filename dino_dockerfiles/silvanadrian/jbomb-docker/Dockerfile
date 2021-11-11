FROM      ubuntu:14.04
MAINTAINER Silvan Adrian "hallo@silvanadrian.ch"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update  > /dev/null && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc && \
    apt-key add rabbitmq-signing-key-public.asc && \
    echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc |sudo apt-key add - && \
    apt-get -qq -y install rabbitmq-server > /dev/null && \
    /usr/sbin/rabbitmq-plugins enable rabbitmq_management && \
    echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config && \
    apt-get install -y software-properties-common python-software-properties && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get -qq update  > /dev/null && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get -qq -y install oracle-java8-installer > /dev/null

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
EXPOSE 5672 15672


RUN wget $(curl -s https://api.github.com/repos/HSR-SE2Proj/jbomberman/releases | grep browser_download_url | grep 'Server[.]jar' | head -n 1 | cut -d '"' -f 4)
CMD service rabbitmq-server start && java -jar *Server.jar
