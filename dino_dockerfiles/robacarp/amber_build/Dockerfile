FROM crystallang/crystal:0.25.0

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && apt-get install -y --no-install-recommends libpq-dev libsqlite3-dev libmysqlclient-dev libreadline-dev git curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y --no-install-recommends nodejs

WORKDIR /amber
COPY shard.yml .
RUN shards build amber
RUN ln -s /amber/bin/amber /usr/local/bin
