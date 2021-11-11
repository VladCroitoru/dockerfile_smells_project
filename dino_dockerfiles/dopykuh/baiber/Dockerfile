FROM ruby

RUN apt update && apt install -y libpq-dev tesseract-ocr poppler-utils postgresql-client
COPY . /srv/baiber
WORKDIR /srv/baiber
RUN gem install bundler --no-user-install
RUN bundle install -j 8 --path=.bundle
RUN bundle exec rails assets:precompile
VOLUME /srv/baiber
CMD bash -c "bundle exec puma -v -t 0:20 -w 10 -p 9292"
