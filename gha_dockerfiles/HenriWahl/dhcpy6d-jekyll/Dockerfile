FROM jekyll/jekyll:4

RUN gem update bundler

RUN wget -O /tmp/Gemfile https://raw.githubusercontent.com/HenriWahl/dhcpy6d-jekyll/main/docs/Gemfile

RUN bundle install --gemfile=/tmp/Gemfile

WORKDIR /jekyll

CMD bundle install && \
    bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload
