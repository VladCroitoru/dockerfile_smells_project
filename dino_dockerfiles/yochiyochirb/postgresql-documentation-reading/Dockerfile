FROM postgres:10.3
MAINTAINER Hirofumi Wakasugi <baenej@gmail.com>

RUN apt-get update -qq && \
    apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    postgresql-server-dev-10

RUN curl -L -O https://ftp.postgresql.org/pub/source/v10.3/postgresql-10.3.tar.gz
RUN tar xvfz postgresql-10.3.tar.gz
RUN mv postgresql-10.3/src/tutorial /postgresql-tutorial
RUN rm -rf postgresql-10.3

WORKDIR /postgresql-tutorial

RUN make
