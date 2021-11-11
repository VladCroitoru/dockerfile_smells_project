FROM ruby
RUN gem install jekyll bundler
WORKDIR /srv/jekyll
COPY ./Gemfile /srv/jekyll/
RUN bundle install
CMD bundle exec jekyll serve --watch --incremental
