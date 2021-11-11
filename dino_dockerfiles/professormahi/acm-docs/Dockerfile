FROM ruby:2.4.2

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs && \
    gem install bundler && \
    rm -rf /var/lib/apt/lists/*

COPY Gemfile Gemfile.lock Rakefile /devdocs/

RUN bundle install --system && \
    rm -rf ~/.gem /root/.bundle/cache /usr/local/bundle/cache

COPY . /devdocs

# Download C++, C, Java8, Python3.5
RUN thor docs:download Cpp C openjdk@8 python@3.5 && \
    thor assets:compile && \
    rm -rf /tmp

EXPOSE 9292
CMD rackup -o 0.0.0.0
