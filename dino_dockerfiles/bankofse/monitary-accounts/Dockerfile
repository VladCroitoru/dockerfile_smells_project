FROM postgres

RUN apt-get update
RUN apt-get install -y libgmp3-dev gcc net-tools curl build-essential wget

RUN apt-get install curl
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

# ADD ./misc/haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz /
ADD https://www.haskell.org/platform/download/2014.2.0.0/haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz /
RUN tar vxf haskell-platform-2014.2.0.0-unknown-linux-x86_64.tar.gz
RUN /usr/local/haskell/ghc-7.8.3-x86_64/bin/activate-hs

ADD ./misc/postgrest-0.2.7.0.tar.xz /postgrest
RUN mv /postgrest/postgrest-0.2.7.0 /usr/local/bin/postgrest
RUN chmod +x /usr/local/bin/postgrest

EXPOSE 3000

# Node Job
RUN mkdir -p /etc/listener/
COPY ./jobs/package.json /etc/listener/package.json
RUN cd /etc/listener && npm install
COPY ./jobs/index.js /etc/listener/index.js

# SQL
COPY ./schema.sql /tmp/schema.sql
COPY ./start_postgrest.sh /docker-entrypoint-initdb.d/start_postgrest.sh
COPY ./setup_db.sh /docker-entrypoint-initdb.d/setup_db.sh
