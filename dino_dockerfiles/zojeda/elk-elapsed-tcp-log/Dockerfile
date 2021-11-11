FROM sebp/elk

WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-filter-elapsed

# overwrite existing file
ADD pipeline.conf /etc/logstash/conf.d/pipeline.conf
