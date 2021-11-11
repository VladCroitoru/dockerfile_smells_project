FROM logstash:2-alpine

COPY logstash.conf gracc-raw-template.json /etc/gracc-stash/

CMD ["-f", "/etc/gracc-stash/logstash.conf","--allow-env"]
