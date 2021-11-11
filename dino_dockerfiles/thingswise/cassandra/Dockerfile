FROM cassandra:3.7

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ADD bootstrap.sh /bootstrap.sh
ADD JSON.sh /JSON.sh

ADD https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64 /dumb-init

RUN chmod +x /bootstrap.sh /JSON.sh /dumb-init

ENTRYPOINT ["/bootstrap.sh"]

CMD ["cassandra", "-f"]
