FROM          ubuntu:latest
MAINTAINER    srangwal@gmail.com

# Install some basic utils
RUN           echo "deb http://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
RUN           sudo apt-get update
RUN           sudo apt-get upgrade -y
RUN           sudo apt-get install -y software-properties-common unzip

# Install Java
RUN           sudo apt-get install -y openjdk-7-jre openjdk-7-jdk
RUN           sudo update-java-alternatives -s java-1.7.0-openjdk-amd64
RUN           sudo ln -s /usr/lib/jvm/java-1.7.0-openjdk-amd64 /usr/lib/jvm/default-java

# For Kafka-manager
RUN           sudo apt-get install -y --allow-unauthenticated sbt
RUN           cd /tmp && git clone https://github.com/yahoo/kafka-manager.git
RUN           cd /tmp/kafka-manager && sbt clean dist && mv ./target/universal/kafka-manager*.zip /opt
RUN           cd /opt && unzip kafka-manager*.zip && ln -s $(find kafka-manager* -type d -prune) kafka-manager

ENV           KAFKA_MANAGER_HOME /opt/kafka-manager

ADD           ./image-files/start-kafka-manager.sh /usr/bin/
CMD           start-kafka-manager.sh

# vim: set nospell:
