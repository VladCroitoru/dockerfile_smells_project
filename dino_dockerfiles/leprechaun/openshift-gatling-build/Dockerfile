FROM denvazh/gatling

ADD entrypoint.sh /entrypoint.sh
RUN apk add --update jq git bash curl

ENTRYPOINT ["bash", "/entrypoint.sh"]
