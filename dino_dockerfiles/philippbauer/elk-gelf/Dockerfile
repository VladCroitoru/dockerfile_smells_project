FROM phusion/baseimage

### install elasticsearch and logstash

ENV KIBANA_VERSION 4.1.0
ENV ELASTICSEARCH_VERSION 1.6
ENV LOGSTASH_VERSION 1.5

RUN apt-get update -qq && apt-get install -qqy curl

RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN add-apt-repository "deb http://packages.elasticsearch.org/elasticsearch/$ELASTICSEARCH_VERSION/debian stable main"
RUN add-apt-repository "deb http://packages.elasticsearch.org/logstash/$LOGSTASH_VERSION/debian stable main"

RUN apt-get update -qq && apt-get install -qqy openjdk-7-jdk elasticsearch logstash


### install kibana

RUN mkdir /opt/kibana \
	&& curl -O https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION-linux-x64.tar.gz \
	&& tar xvf kibana-$KIBANA_VERSION-linux-x64.tar.gz -C /opt/kibana --strip-components=1 \
	&& rm -f kibana-$KIBANA_VERSION-linux-x64.tar.gz


### configure elasticsearch

ADD ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml


### configure logstash

ADD ./logstash-gelf-input.conf /etc/logstash/conf.d/logstash-gelf-input.conf
ADD ./logstash-elasticsearch-output.conf /etc/logstash/conf.d/logstash-elasticsearch-output.conf


### configure kibana

RUN mkdir /var/log/kibana


### install start-up script

RUN mkdir /etc/service/elk-logback
ADD ./run.sh /etc/service/elk-logback/run
RUN chmod +x /etc/service/elk-logback/run

### volume with elasticsearch-data
VOLUME ["/var/lib/elasticsearch/elasticsearch"]


### start up everthing

EXPOSE 9200 5601 12201

CMD [ "/sbin/my_init" ]
