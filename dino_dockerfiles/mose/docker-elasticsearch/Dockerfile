FROM mose/faria-basedock
MAINTAINER mose <mose@mose.com>

RUN apt-get -y -qq update > /dev/null
RUN apt-get install -y python-software-properties > /dev/null
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get -y -qq update > /dev/null
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt-get install -y oracle-java7-installer > /dev/null

ENV ELASTICSEARCH_VERSION 0.90.11
RUN mkdir /elasticsearch
RUN curl -o /tmp/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz -s https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
RUN tar xzf /tmp/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
RUN mv elasticsearch-$ELASTICSEARCH_VERSION /elasticsearch/src
ADD files/elasticsearch.yml /elasticsearch/etc/elasticsearch.yml
ADD files/supervisord-elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

WORKDIR /elasticsearch/src/bin

# https://github.com/royrusso/elasticsearch-HQ
# -> http://localhost:9200/_plugin/HQ/
RUN ./plugin -install royrusso/elasticsearch-HQ

# https://github.com/jprante/elasticsearch-knapsack
# this one is for v0.90.11, change it if you change version
RUN ./plugin -install knapsack -url http://bit.ly/1mlzYoB

# http://mobz.github.io/elasticsearch-head/
# -> http://localhost:9200/_plugin/head/
RUN ./plugin -install mobz/elasticsearch-head

# http://bigdesk.org/
# -> http://localhost:9200/_plugin/ibigdesk/
RUN ./plugin -install lukas-vlcek/bigdesk

# https://github.com/polyfractal/elasticsearch-inquisitor
# -> http://localhost:9200/_plugin/inquisitor/
RUN ./plugin -install polyfractal/elasticsearch-inquisitor

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9200
EXPOSE 9300

CMD /usr/bin/supervisord -n
