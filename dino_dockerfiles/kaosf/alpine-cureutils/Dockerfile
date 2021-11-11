FROM inzinger/alpine-ruby
MAINTAINER ka <ka.kaosf@gmail.com>
RUN apk --update --no-cache add ca-certificates git ruby-json ruby-bigdecimal && \
  rm -rf /var/cache/apk/* && \
  git clone https://github.com/greymd/cureutils.git && \
  cd cureutils && \
  gem install bundler rake && \
  bundle install && \
  rake build && \
  find ./pkg/ -type f | head -n 1 | xargs gem install && \
  cd .. && \
  rm -rf cureutils
