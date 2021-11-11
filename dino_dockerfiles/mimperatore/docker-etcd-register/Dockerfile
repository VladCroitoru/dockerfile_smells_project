FROM ruby:2.1-onbuild
MAINTAINER mimperatore@gmail.com

VOLUME ["/var/run/docker.sock"]

ENV DOCKER_HOST unix:///var/run/docker.sock

ONBUILD RUN bundle exec rspec

CMD ["./register.rb"]
