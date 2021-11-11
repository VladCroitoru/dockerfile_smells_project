FROM jwilder/docker-gen:0.7.3
RUN apk add --no-cache curl jq
COPY endpoints.tmpl ./
COPY zabbix-notify.sh ./
CMD ["-watch", "-notify", "./zabbix-notify.sh", "./endpoints.tmpl", "./endpoints.list"]
