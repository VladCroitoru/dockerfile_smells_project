FROM ruby:2.4.1

WORKDIR /app

RUN git clone https://github.com/Apexal/conexus.git .
RUN bundle install

CMD ruby ./bot.rb $TOKEN $CLIENT_ID