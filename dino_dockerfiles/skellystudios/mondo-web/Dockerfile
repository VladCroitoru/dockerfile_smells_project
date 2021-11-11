FROM ruby
COPY Gemfile .
RUN bundle install
ADD . .
RUN bundle install
CMD rails s -b 0.0.0.0
