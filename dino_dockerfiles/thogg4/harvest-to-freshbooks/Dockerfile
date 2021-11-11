FROM ruby:2.2.3

RUN gem install ruby-freshbooks
RUN gem install harvested

RUN mkdir /scripts/
COPY script.rb /scripts/

CMD ["ruby", "/scripts/script.rb"]
