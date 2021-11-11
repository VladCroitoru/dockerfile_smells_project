FROM logstash:2.1.0
MAINTAINER Ludek Vesely <ludek.vesely@email.com>

EXPOSE 5000/tcp 5000/udp
CMD ["logstash", "-f", "/logstash.conf"]
ENTRYPOINT ["/run.sh"]

ENV ELASTICSEARCH_HOSTS elasticsearch:9200
ENV ELASTICSEARCH_USER foo
ENV ELASTICSEARCH_PASSWORD bar

ENV DROP_NON_JSON false
ENV STDOUT true
ENV LOGSPOUT ignore

ADD run.sh /run.sh
RUN chmod +x /run.sh

ADD logstash.conf /logstash.conf

