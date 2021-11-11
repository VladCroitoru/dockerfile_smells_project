FROM ruby:2.6

EXPOSE 3000

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs

WORKDIR /opt/trln_argon

RUN bundle install && bundle exec rake engine_cart:prepare

CMD cd /opt/trln_argon && ./docker-start.sh
#bundle exec rake engine_cart:server['-b 0.0.0.0']


