FROM ruby:2.4.1-alpine

RUN gem install serverspec \
    && gem install rake 

WORKDIR /serverspec

CMD /usr/local/bin/rake
