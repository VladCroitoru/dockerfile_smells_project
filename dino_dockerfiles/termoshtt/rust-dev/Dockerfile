FROM rust:1.25
MAINTAINER termoshtt <toshiki.teramura@gmail.com>
RUN apt-get update -qq && apt-get -y -qq install \
  curl gcc gfortran make cmake binutils-dev \
  sqlite3 libsqlite3-dev \
  libcurl4-openssl-dev libelf-dev libdw-dev libiberty-dev \
  && apt-get clean
