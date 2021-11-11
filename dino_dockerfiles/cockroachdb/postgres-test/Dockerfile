FROM java:openjdk-8

# The forward reference version is the oldest version from which we
# support upgrading. The bidirectional reference version is the oldest
# version that we support upgrading from and downgrading to.
ENV FORWARD_REFERENCE_VERSION="beta-20170413"
ENV BIDIRECTIONAL_REFERENCE_VERSION="beta-20170413"

# Debian's stock node package doesn't include npm.
RUN curl -fsSL https://deb.nodesource.com/setup_6.x | bash - && \
	apt-get update -y && \
	apt-get upgrade -y

# Prereqs for dotnet
RUN apt-get install -y \
	curl \
	libunwind8 \
	gettext \
	apt-transport-https

# Register the trusted Microsoft Product Key and Product Feed
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
	mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
	sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-jessie-prod jessie main" > /etc/apt/sources.list.d/dotnetdev.list'

# The basics
RUN apt-get update -y && \
  apt-get install -y \
	git \
	libpq-dev \
	postgresql \
	vim

# acceptance/cli_test.go
RUN apt-get install -y \
	expect

# C
RUN apt-get install -y \
	gcc \
	libpqtypes-dev

# Node
RUN apt-get install -y \
	nodejs

RUN npm install -g pg@7.3.0 mocha@4.0.1 pg-error-codes@1.0.0

# Python
RUN apt-get install -y \
	python-pip \
	python-dev

# PHP
RUN apt-get install -y \
	php5-cli \
	php5-pgsql

# dotnet
RUN apt-get install -y \
	dotnet-sdk-2.0.0 \
	nuget

RUN pip install psycopg2

# Ruby
RUN mkdir ruby-install && \
	curl -fsSL https://github.com/postmodern/ruby-install/archive/v0.6.1.tar.gz | tar --strip-components=1 -C ruby-install -xz && \
	make -C ruby-install install && \
	ruby-install --system ruby 2.4.0 && \
	gem update --system

# Ruby acceptance tests
RUN gem install pg

# Java/Maven

# There doesn't appear to be a good way to install maven via apt-get on the
# base image we're running off of.
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz https://apache.osuosl.org/maven/maven-3/3.6.0/binaries/apache-maven-3.6.0-bin.tar.gz \
  && echo "6a1b346af36a1f1a491c1c1a141667c5de69b42e6611d3687df26868bc0f4637  /tmp/apache-maven.tar.gz" | sha256sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

# This pom.xml mirrors the one in the main Cockroach repo at pkg/acceptance/testdata/java.
RUN echo '<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"> <modelVersion>4.0.0</modelVersion> <groupId>java</groupId> <artifactId>java</artifactId> <version>1.0-SNAPSHOT</version> <dependencies> <dependency> <groupId>junit</groupId> <artifactId>junit</artifactId> <version>4.8.1</version> </dependency> <dependency> <groupId>org.postgresql</groupId> <artifactId>postgresql</artifactId> <version>42.1.4</version> </dependency> <dependency> <groupId>org.apache.maven.surefire</groupId> <artifactId>surefire-junit4</artifactId> <version>2.12.4</version> </dependency> <dependency> <groupId>org.apache.maven</groupId> <artifactId>maven-profile</artifactId> <version>2.0.6</version> </dependency> <dependency> <groupId>org.apache.maven</groupId> <artifactId>maven-repository-metadata</artifactId> <version>2.0.6</version> </dependency> <dependency> <groupId>org.apache.maven</groupId> <artifactId>maven-plugin-registry</artifactId> <version>2.0.6</version> </dependency> <dependency> <groupId>classworlds</groupId> <artifactId>classworlds</artifactId> <version>1.1-alpha-2</version> </dependency> </dependencies> <build> <testSourceDirectory>src/main</testSourceDirectory> </build> </project> ' > pom.xml

RUN mvn test

RUN rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 -b fatjartests https://github.com/cockroachdb/finagle-postgres.git && \
	cd /finagle-postgres && \
	./sbt assembly && \
	mv target/scala-2.11/finagle-postgres-tests.jar / && \
	cd / && rm -rf /finagle-postgres ~/.ivy2

# Download a reference binary that forward tests can run against.
RUN mkdir /forward-reference-version && \
	curl -SL https://binaries.cockroachdb.com/cockroach-${FORWARD_REFERENCE_VERSION}.linux-amd64.tgz | tar xvz -C /tmp && \
	mv /tmp/cockroach-${FORWARD_REFERENCE_VERSION}*/* /forward-reference-version

# Download a reference binary that bidirectional tests can run against.
RUN mkdir /bidirectional-reference-version && \
	curl -SL https://binaries.cockroachdb.com/cockroach-${BIDIRECTIONAL_REFERENCE_VERSION}.linux-amd64.tgz | tar xvz -C /tmp && \
	mv /tmp/cockroach-${BIDIRECTIONAL_REFERENCE_VERSION}*/* /bidirectional-reference-version

# Install Go compiler, needed for examples-orms tests.
RUN curl https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz -o golang.tar.gz \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz

# Install npgsql and create a local a feed.
RUN mkdir /nuget && \
  echo '<?xml version="1.0" encoding="utf-8"?><configuration><packageSources><add key="local-packages" value="." /></packageSources></configuration>' > /nuget/NuGet.Config && \
	curl -fsSL https://www.nuget.org/api/v2/package/Npgsql/3.2.5 > /nuget/npgsql.3.2.5.nupkg

ENV PATH /usr/local/go/bin:$HOME/dotnet:$PATH
