FROM debian:jessie
MAINTAINER Daniel Pinto <cayan@programmer.net>

RUN apt-get update && apt-get install -y \
                g++ \
                make \
                autoconf \
                automake \
                pkg-config \
                libxml2-dev \
                lua-sql-mysql \
                lua-sql-mysql-dev \
                liblua5.1-0-dev \
                libgmp3-dev \
                libboost-all-dev \
                libmysqlclient-dev \
        --no-install-recommends && rm -r /var/lib/apt/lists/*

WORKDIR /server
