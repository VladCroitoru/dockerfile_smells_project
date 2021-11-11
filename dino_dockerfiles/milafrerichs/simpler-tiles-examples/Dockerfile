FROM milafrerichs/simple-tiles-ruby:0.6.0

RUN mkdir /tileserver
WORKDIR /tileserver
ADD Gemfile /tileserver/Gemfile
RUN bundle install
ADD . /tileserver

EXPOSE 9292
CMD ["puma"]
