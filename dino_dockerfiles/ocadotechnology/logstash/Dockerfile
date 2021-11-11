FROM logstash:2.4

USER logstash

COPY 01-input.conf  /config/01-input.conf
COPY 02-filter.conf /config/02-filter.conf
COPY 03-output.conf /config/03-output.conf

ENTRYPOINT ["logstash"]
CMD ["--allow-env", "-f", "/config"]
