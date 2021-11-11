FROM ruby:2.5
RUN apt-get update && apt-get install -y \
    python-pip \
    python-dev && \
    pip install --upgrade awscli && \
    rm -rf /var/lib/apt/lists/*
ADD ./Gemfile /code/Gemfile
WORKDIR /code
RUN bundle install
ADD . /code
CMD bundle exec ruby ./ec2metadata.rb
