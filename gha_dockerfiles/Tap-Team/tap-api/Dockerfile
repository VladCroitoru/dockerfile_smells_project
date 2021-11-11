FROM ruby:3.0.1

RUN apt-get update && apt-get install -y build-essential nodejs \
 && wget https://dist.ipfs.io/go-ipfs/v0.10.0/go-ipfs_v0.10.0_linux-amd64.tar.gz \
 && tar -xvzf go-ipfs_v0.10.0_linux-amd64.tar.gz \
 && cd go-ipfs \
 && bash install.sh \
 && cd .. \
 && rm -rf go-ipfs_v0.10.0_linux-amd64.tar.gz \
 && rm -rf go-ipfs \
 && ipfs init \
 && mkdir /tap-api

WORKDIR /tap-api

COPY Gemfile /tap-api/Gemfile
COPY Gemfile.lock /tap-api/Gemfile.lock

RUN gem install bundler:2.2.24 \
 && bundle install

COPY . /tap-api