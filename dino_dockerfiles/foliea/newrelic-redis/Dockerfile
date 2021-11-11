FROM ubuntu:14.04

MAINTAINER Adrien Folie <folie.adrien@gmail.com>

# Set ruby version.
ENV RUBY_MAJOR 2.1
ENV RUBY_MINOR 2.1.2

# Install dependencies.
RUN apt-get update -qq && \
    apt-get install -qy \
    git-core \
    curl \
    wget \
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
    python-software-properties

# Install ruby.
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_MINOR.tar.gz && \
    tar -xzvf ruby-$RUBY_MINOR.tar.gz && \
    cd ruby-$RUBY_MINOR && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-$RUBY_MINOR ruby-$RUBY_MINOR.tar.gz && \
    echo "gem: --no-document" > /usr/local/etc/gemrc

# Install bundler.
RUN gem install bundler

# Set newrelic_redis_plugin version
ENV PLUGIN_VERSION 1.0.1

# Get newrelic redis plugin.
RUN wget https://github.com/kenjij/newrelic_redis_plugin/archive/v$PLUGIN_VERSION.tar.gz && \
    tar -xzvf v$PLUGIN_VERSION.tar.gz  && \
    rm v$PLUGIN_VERSION.tar.gz && \
    mv newrelic_redis_plugin-$PLUGIN_VERSION newrelic

# Install gem dependencies.
RUN cd newrelic && bundle install

# Add user 'agent'.
RUN useradd agent

# Give plugin app acess to 'agent'.
RUN chown -R agent:agent newrelic

# Switch to user 'agent'.
USER agent

# Copy plugin config file to config directory.
COPY newrelic_plugin.yml newrelic/config/newrelic_plugin.yml

# Set current directory to plugin app's location.
WORKDIR newrelic

# Start newrelic redis agent.
CMD ["./newrelic_redis_agent"]
