FROM docker.elastic.co/logstash/logstash:5.3.1

USER root

RUN rm -f /usr/share/logstash/pipeline/logstash.conf
RUN rm -f /usr/share/logstash/config/logstash.yml
ADD logstash.conf /usr/share/logstash/pipeline/logstash.conf
ADD logstash.yml /usr/share/logstash/config/

# Place the startup wrapper script.
ADD docker-entrypoint /usr/local/bin/
RUN chmod 0755 /usr/local/bin/docker-entrypoint

#USER logstash

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
CMD ["-f", "/usr/share/logstash/pipeline/"]
