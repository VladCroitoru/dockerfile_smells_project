FROM ruby:2.1.2

RUN gem install selenium && selenium install && gem install selenium-webdriver 

ADD ./scripts/ /home/root/scripts

ENTRYPOINT ["/home/root/scripts/loadme.rb"]
