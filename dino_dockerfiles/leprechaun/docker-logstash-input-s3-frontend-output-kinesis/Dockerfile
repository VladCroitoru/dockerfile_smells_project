FROM logstash:2

RUN /opt/logstash/bin/plugin install logstash-input-s3
RUN /opt/logstash/bin/plugin install logstash-output-kinesis
RUN /opt/logstash/bin/plugin install logstash-filter-de_dot

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
COPY logstash.conf.tpl /config/logstash.conf.tpl

CMD ["/entrypoint.sh"]
