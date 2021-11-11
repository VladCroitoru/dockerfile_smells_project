FROM ruby:2.2.0

RUN mkdir /opt/backkeep
COPY . /opt/backkeep/

ENTRYPOINT ["ruby", "/opt/backkeep/lib/backup.rb"]
