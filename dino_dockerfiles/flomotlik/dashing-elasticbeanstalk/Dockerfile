FROM phusion/passenger-ruby21

RUN gem install bundler

ADD Gemfile /home/app/Gemfile
ADD Gemfile.lock /home/app/Gemfile.lock
WORKDIR /home/app
RUN bundle install

ADD . /home/app

EXPOSE 3030
CMD ["/home/app/start_dashing.sh"]
