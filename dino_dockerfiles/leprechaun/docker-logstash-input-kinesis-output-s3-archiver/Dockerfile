FROM logstash:2

RUN /opt/logstash/bin/plugin install logstash-input-kinesis
RUN /opt/logstash/bin/plugin install logstash-output-s3

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
COPY logstash.conf.tpl /config/logstash.conf.tpl

CMD ["/entrypoint.sh"]
