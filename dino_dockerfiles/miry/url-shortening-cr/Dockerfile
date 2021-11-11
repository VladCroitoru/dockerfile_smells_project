FROM crystallang/crystal:0.26.1 as builder

ENV KEMAL_ENV=production

WORKDIR /app
ADD ./shard.yml /app/shard.yml
ADD ./shard.lock /app/shard.lock
RUN shards install

ADD ./src /app/src
RUN crystal build --release src/server.cr

# FROM crystallang/crystal:0.24.1
FROM ubuntu:xenial
RUN \
  apt-get update && \
  apt-get install -y libssl-dev libxml2-dev libyaml-dev libgmp-dev libevent-dev && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /app
COPY --from=builder /app/server .

EXPOSE 3000
CMD ["/app/server"]
