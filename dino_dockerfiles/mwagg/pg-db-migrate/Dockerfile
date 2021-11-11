FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y curl python

RUN mkdir -p /usr/local/node
RUN curl -L http://nodejs.org/dist/v0.10.26/node-v0.10.26-linux-x64.tar.gz | \
  tar xzf - -C /usr/local/node --strip-components=1

ENV PATH $PATH:/usr/local/node/bin

RUN mkdir -p /usr/local/pg-db-migrate

RUN cd /usr/local/pg-db-migrate; npm install pg db-migrate

ADD wait_for_pg /usr/local/pg-db-migrate/wait_for_pg
ADD migrate /usr/local/pg-db-migrate/migrate
ADD write_config /usr/local/pg-db-migrate/write_config

ENTRYPOINT ["/usr/local/pg-db-migrate/migrate"]
