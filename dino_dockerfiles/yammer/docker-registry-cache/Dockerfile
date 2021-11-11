FROM alpine:3.6

RUN apk update && apk add squid bash
COPY ./squid.conf /etc/squid.conf
COPY ./start.sh /bin/start.sh

RUN chmod +x /bin/start.sh

ENV CACHE_SIZE_MB=10000 TARGET_REGISTRY_IP=172.17.0.1 TARGET_REGISTRY_PORT=443

CMD [ "/bin/start.sh" ]