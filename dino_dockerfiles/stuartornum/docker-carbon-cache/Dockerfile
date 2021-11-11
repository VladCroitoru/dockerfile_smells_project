FROM python:2.7-slim

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install graphite-carbon -y && apt-get clean all

RUN echo "CARBON_CACHE_ENABLED=true" > /etc/default/graphite-carbon

ENTRYPOINT ["/usr/bin/python", "/usr/bin/carbon-cache", "--debug", "--config=/data/carbon/carbon.conf", "--pidfile=/tmp/carbon-cache.pid", "start"]
USER _graphite
EXPOSE 8080

