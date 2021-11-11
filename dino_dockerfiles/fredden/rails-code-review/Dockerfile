FROM ruby:alpine

RUN apk add --no-cache build-base

RUN gem install brakeman
RUN gem install rubocop
RUN gem install rails_best_practices
RUN gem install rubycritic

WORKDIR /var/app

CMD ["sh", "-c", "brakeman -Aqz --no-pager && \
                  rubocop -RF && \
                  rubycritic -f console -s 80 && \
                  rails_best_practices"]
