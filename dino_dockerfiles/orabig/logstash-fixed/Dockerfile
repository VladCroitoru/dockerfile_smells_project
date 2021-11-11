FROM logstash:2.0.0-1

MAINTAINER benoit.chauvet@gmail.com

RUN /opt/logstash/bin/plugin install --version 0.9.6 logstash-input-beats

ENTRYPOINT ["/opt/logstash/bin/logstash"]
CMD ["--help"]
