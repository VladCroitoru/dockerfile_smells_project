FROM openaustralia/morph-ruby
MAINTAINER Chris Mytton <chrismytton@gmail.com>

# Pry is handy to have installed when debugging scrapers.
RUN bash -l -c "gem install pry --no-rdoc --no-ri"

COPY ./docker-entrypoint /
ENTRYPOINT ["/docker-entrypoint"]
WORKDIR /repo
CMD ["ruby", "-r/usr/local/lib/prerun.rb", "scraper.rb"]
