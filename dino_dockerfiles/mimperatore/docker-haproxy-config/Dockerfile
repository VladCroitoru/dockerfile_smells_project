FROM ruby:2.1-onbuild
MAINTAINER mimperatore@gmail.com

#VOLUME ["/etc/haproxy"]

ONBUILD RUN bundle exec rspec

CMD ["./haproxy-config.rb"]
