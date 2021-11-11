FROM crystallang/crystal:0.23.1

ENV KEMAL_ENV=production

ADD ./shard.yml /app/shard.yml
WORKDIR /app
RUN shards install

ADD . /app
RUN crystal build src/bundle-server.cr

EXPOSE 3000

ENTRYPOINT /app/bundle-server
