FROM ruby:2.7
RUN gem install bundler
WORKDIR /usr/src/app
COPY . .
RUN bundle install
RUN rm -r pkg | bundle exec rake build orochi_for_medusa.gemspec
RUN gem install pkg/orochi-for-medusa-*.gem
ARG UID=1001
ARG GID=1001

RUN addgroup -gid ${GID} medusa && useradd -m --shell /bin/sh --gid ${GID} --uid ${UID} medusa 
USER medusa
WORKDIR /home/medusa
#CMD ["/bin/bash"]
