FROM docker:1.9-dind
RUN apk add --update bash py-pip && rm -rf /var/cache/apk/*
RUN pip install docker-compose

COPY dind-isolated-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["dind-isolated-entrypoint.sh"]
CMD []
