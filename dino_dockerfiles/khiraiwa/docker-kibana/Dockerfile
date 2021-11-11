FROM ubuntu:14.04.3

MAINTAINER khiraiwa

ENV KIBANA_VERSION 4.2.0
ENV MARVEL_VERSION 2.0.0

# Install Java
RUN \
  apt-get update && \
  apt-get install software-properties-common python-software-properties wget unzip -y --no-install-recommends && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer --no-install-recommends && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Add kibana user
RUN \
  mkdir -p /home/kibana/ && \
  groupadd -r kibana && useradd -r -d /home/kibana -s /bin/bash -g kibana kibana && \
  echo 'kibana ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Install Kibana
RUN \
  cd /home/kibana && \
  wget http://download.elastic.co/kibana/kibana-snapshot/kibana-${KIBANA_VERSION}-snapshot-linux-x64.zip && \
  unzip kibana-${KIBANA_VERSION}-snapshot-linux-x64.zip && \
  rm -f kibana-${KIBANA_VERSION}-snapshot-linux-x64.zip

# Install Marvel plugin
RUN \
  cd /home/kibana && \
  wget https://download.elastic.co/elasticsearch/marvel/marvel-${MARVEL_VERSION}.tar.gz && \
  /home/kibana/kibana-${KIBANA_VERSION}-snapshot-linux-x64/bin/kibana plugin --install marvel --url file:///home/kibana/marvel-${MARVEL_VERSION}.tar.gz && \
  rm -f marvel-${MARVEL_VERSION}.tar.gz

ADD config/kibana.yml /home/kibana/kibana-${KIBANA_VERSION}-snapshot-linux-x64/config/kibana.yml

RUN mkdir -p /data_kibana/
VOLUME ["/data_kibana/"]

# Mount data dir and setup home dir
RUN \
  chown -R kibana:kibana /data_kibana && \
  chown -R kibana:kibana /home/kibana

USER kibana
WORKDIR /home/kibana/kibana-${KIBANA_VERSION}-snapshot-linux-x64
EXPOSE 5601
CMD \
  sed -i -e"s|ELASTICSEARCH_HOST|${ELASTICSEARCH_HOST}|g" /home/kibana/kibana-${KIBANA_VERSION}-snapshot-linux-x64/config/kibana.yml && \
  sudo chown -R kibana:kibana /data_kibana && \
  /home/kibana/kibana-${KIBANA_VERSION}-snapshot-linux-x64/bin/kibana
