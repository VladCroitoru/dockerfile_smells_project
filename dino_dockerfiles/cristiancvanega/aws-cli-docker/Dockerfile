FROM ubuntu:14.04

WORKDIR /root

RUN apt-get update && \
	apt-get install -y \
	git-core \
	curl \
	zlib1g-dev \
	build-essential \
	libssl-dev \
	libreadline-dev \
	libyaml-dev \
	libsqlite3-dev \
	sqlite3 \
	libxml2-dev \
	libxslt1-dev \
	libcurl4-openssl-dev \
	python-software-properties \
	libffi-dev

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash && \
	apt-get install -y \
	nodejs && \
	npm install

ENV RUBY_VERSION 2.4.0

RUN	["/bin/bash", "-c", "git clone https://github.com/rbenv/rbenv.git ~/.rbenv"]
RUN	["/bin/bash", "-c", "git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build"]
RUN .rbenv/bin/rbenv install "$RUBY_VERSION" && \
	.rbenv/versions/"$RUBY_VERSION"/bin/ruby -v && \
	.rbenv/versions/"$RUBY_VERSION"/bin/gem install bundler

RUN apt-get install -y python-dev && \
	curl -O https://bootstrap.pypa.io/get-pip.py && \
	python get-pip.py --user && \
	.local/bin/pip  install awscli --upgrade --user

RUN mv .local/bin/aws /usr/local/bin/