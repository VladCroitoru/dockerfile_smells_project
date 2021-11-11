FROM marvinoeben/c7-systemd

MAINTAINER Marvin Oeben "oebenmarvin@gmail.com"

# Install dependencies & clean
RUN yum update -y && yum install -y \
    sudo \
    java-1.8.0-openjdk-devel \
    nano \
    git-all \
    wget \
    zip unzip \
    bind bind-utils
RUN yum clean all

# Download and install Elasticsearch
RUN wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/rpm/elasticsearch/2.3.4/elasticsearch-2.3.4.rpm
RUN rpm -ivh elasticsearch-2.3.4.rpm
RUN systemctl enable elasticsearch.service

# Download and install the image plugin
RUN git clone https://github.com/kiwionly/elasticsearch-image /usr/share/elasticsearch/elasticsearch-image
RUN ls /usr/share/elasticsearch

# Export java version:
RUN export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.102-1.b14.el7_2.x86_64/
RUN export PATH=$JAVA_HOME/bin:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.102-1.b14.el7_2.x86_64/

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.102-1.b14.el7_2.x86_64
# Download and install gradle:
COPY install-gradle-centos.sh /
RUN sh install-gradle-centos.sh

WORKDIR "/usr/share/elasticsearch/elasticsearch-image"
RUN ls -l
RUN chmod 777 gradlew
RUN ./gradlew plugin

WORKDIR "/"

## FROM ELASTICSEARCH DOCKER:

ENV PATH /usr/share/elasticsearch/bin:$PATH

WORKDIR /usr/share/elasticsearch

RUN set -ex \
	&& for path in \
		./data \
		./logs \
		./config \
		./config/scripts \
	; do \
		mkdir -p "$path"; \
		chown -R elasticsearch:elasticsearch "$path"; \
	done

COPY config ./config

VOLUME /usr/share/elasticsearch/data

COPY docker-entrypoint.sh /

## Added to make the entrypoint work:
# Setup gosu for easier command execution
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && rm -r /root/.gnupg/ \
    && chmod +x /usr/local/bin/gosu

# Install head plugin
RUN \
  cd /usr/share/elasticsearch && \
    bin/plugin install mobz/elasticsearch-head

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
