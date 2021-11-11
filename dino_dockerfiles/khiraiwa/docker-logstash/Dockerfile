FROM ubuntu:14.04.3

MAINTAINER khiraiwa

ENV AWS_ACCESS_KEY_ID dummy
ENV AWS_SECRET_ACCESS_KEY dummy
ENV LOGSTASH_VERSION 2.0.0

# Install Java
RUN \
  apt-get update && \
  apt-get install software-properties-common python-software-properties wget unzip git -y --no-install-recommends && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer --no-install-recommends && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Add logstash user
RUN \
  mkdir -p /home/logstash/ && \
  groupadd -r logstash && useradd -r -d /home/logstash -s /bin/bash -g logstash logstash && \
  echo 'logstash ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Install Logstash
RUN \
  cd /home/logstash && \
  wget https://download.elastic.co/logstash/logstash/logstash-${LOGSTASH_VERSION}.zip && \
  unzip logstash-${LOGSTASH_VERSION}.zip && \
  rm -f logstash-${LOGSTASH_VERSION}.zip

ADD logstash.conf /home/logstash/logstash-${LOGSTASH_VERSION}/logstash.conf

# Install plugin
COPY logstash-input-cloudwatch-0.2.2.gem /home/logstash/logstash-input-cloudwatch-0.2.2.gem
RUN \
  /home/logstash/logstash-${LOGSTASH_VERSION}/bin/plugin install /home/logstash/logstash-input-cloudwatch-0.2.2.gem && \
  rm -f /home/logstash/logstash-input-cloudwatch-0.2.2.gem

RUN mkdir -p /data_logstash/
VOLUME ["/data_logstash/"]

# Mount data dir and setup home dir
RUN \
  chown -R logstash:logstash /data_logstash && \
  chown -R logstash:logstash /home/logstash

USER logstash
WORKDIR /home/logstash/logstash-${LOGSTASH_VERSION}

CMD \
  sudo chown -R logstash:logstash /data_logstash && \
  sed -i -e"s|ELASTICSEARCH_HOST|${ELASTICSEARCH_HOST}|g" /home/logstash/logstash-${LOGSTASH_VERSION}/logstash.conf && \
  if [ ! -e /data_logstash/logstash.conf ]; then \
    cp /home/logstash/logstash-${LOGSTASH_VERSION}/logstash.conf /data_logstash/logstash.conf; \
  fi && \
  /home/logstash/logstash-${LOGSTASH_VERSION}/bin/logstash agent -f /data_logstash/logstash.conf
