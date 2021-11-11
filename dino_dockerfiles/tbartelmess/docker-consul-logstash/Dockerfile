FROM logstash:5.0
COPY docker-entrypoint.sh /

RUN echo "path.config: /etc/logstash/conf.d" >> /etc/logstash/logstash.yml
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["-e", "agent"]
