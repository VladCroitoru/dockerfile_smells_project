FROM ruby:2.4.1

RUN apt-get update && apt-get install -y vim mecab mecab-ipadic-utf8 libmecab-dev locales locales-all
RUN gem install sinatra natto thor
RUN git clone https://github.com/suzuki86/rhymer.git
WORKDIR /rhymer
RUN bundle install && gem build rhymer.gemspec && gem install rhymer-0.0.4.gem

ENV LANG=ja_JP.UTF-8
COPY server.rb server.rb

CMD ["ruby", "server.rb", "-p", "4567", "-o", "0.0.0.0"]
