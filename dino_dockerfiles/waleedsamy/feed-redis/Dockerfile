FROM redis:3

WORKDIR /feed

ADD tab2json.awk /feed/tab2json.awk

ADD docker-entrypoint.sh /feed/docker-entrypoint.sh

ENTRYPOINT ["/feed/docker-entrypoint.sh"]
