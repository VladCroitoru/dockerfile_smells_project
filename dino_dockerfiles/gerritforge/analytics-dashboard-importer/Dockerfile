FROM taskrabbit/elasticsearch-dump:v3.3.1

RUN apk add --no-cache curl

COPY docker-entrypoint.sh wait-for-elasticsearch /
COPY ./elasticsearch-config/ /elasticsearch-config/
COPY ./kibana-config/ /kibana-config/

ENTRYPOINT /docker-entrypoint.sh
