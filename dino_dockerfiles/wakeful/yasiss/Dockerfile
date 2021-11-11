FROM centos:7

MAINTAINER AJ <aj@laatu.uk>

RUN yum install -y ruby
RUN gem install bundler

RUN mkdir -p /app
COPY Gemfile /app/
COPY app.rb /app/
RUN cd /app && bundle install

EXPOSE 8080

CMD ["/usr/bin/ruby", "/app/app.rb"]
