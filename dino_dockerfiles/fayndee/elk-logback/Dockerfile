FROM phusion/baseimage
MAINTAINER Fang Yuan <fayndee@hotmail.com>


### install elasticsearch and logstash

RUN apt-get update -qq && apt-get install -qqy curl

RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN add-apt-repository "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"
RUN add-apt-repository "deb http://packages.elasticsearch.org/logstash/1.4/debian stable main"

RUN apt-get update -qq && apt-get install -qqy openjdk-7-jdk elasticsearch logstash


### install kibana

RUN mkdir /opt/kibana \
	&& curl -O https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-linux-x64.tar.gz \
	&& tar xvf kibana-4.0.0-linux-x64.tar.gz -C /opt/kibana --strip-components=1 \
	&& rm -f kibana-4.0.0-linux-x64.tar.gz


### configure elasticsearch

ADD ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml


### configure logstash

ADD ./logstash-tcp-input.conf /etc/logstash/conf.d/logstash-tcp-input.conf
ADD ./logstash-udp-input.conf /etc/logstash/conf.d/logstash-udp-input.conf
ADD ./logstash-elasticsearch-output.conf /etc/logstash/conf.d/logstash-elasticsearch-output.conf


### configure kibana

RUN mkdir /var/log/kibana


### install start-up script

RUN mkdir /etc/service/elk-logback
ADD ./run.sh /etc/service/elk-logback/run
RUN chmod +x /etc/service/elk-logback/run


### start up everthing

EXPOSE 9200 4560 4570/udp 5601

CMD [ "/sbin/my_init" ]