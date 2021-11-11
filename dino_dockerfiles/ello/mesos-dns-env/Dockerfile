FROM mesosphere/mesos-dns:latest
MAINTAINER Jay Zeschin <jay@ello.co>

RUN curl -o /usr/local/bin/jq -SL http://stedolan.github.io/jq/download/linux64/jq && chmod +x /usr/local/bin/jq

COPY config-template.json .
COPY mesos-dns.sh .

CMD ["./mesos-dns.sh"]

