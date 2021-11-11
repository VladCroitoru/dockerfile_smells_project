FROM logstash:2.3

# Make .m2 accessible to logstash user, otherwise logstash won't start
RUN mkdir -p /var/lib/logstash/.m2
RUN ln -s /var/lib/logstash/.m2 /root/.m2

ENV PATH /opt/logstash/vendor/jruby/bin/:$PATH
RUN gem install logstash-input-dynamodb:'> 2' logstash-filter-dynamodb:'> 2'
RUN plugin install logstash-input-dynamodb logstash-filter-dynamodb logstash-output-amazon_es
