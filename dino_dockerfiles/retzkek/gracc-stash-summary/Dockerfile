FROM logstash:2.3

COPY logstash.conf gracc-summary-template.json /etc/gracc-stash/

CMD ["-f", "/etc/gracc-stash/logstash.conf","--allow-env"]
