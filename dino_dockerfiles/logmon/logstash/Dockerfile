# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash:5.6.3

COPY config/logstash.yml /usr/share/logstash/config/logstash.yml
COPY logstash-output-pushgateway-0.1.0.gem /usr/share/logstash/

RUN logstash-plugin install logstash-output-pushgateway-0.1.0.gem
RUN logstash-plugin update logstash-input-beats
# COPY pipeline/logstash.conf /usr/share/logstash/pipeline/
# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
