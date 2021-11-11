FROM ruby:2.6.3

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get update -qq && \
    apt-get install -y build-essential \ 
		      vim \
                       libpq-dev \        
                       nodejs mariadb-client   

RUN mkdir /app_name 

ENV APP_ROOT /app_name 
WORKDIR $APP_ROOT

ADD ./Gemfile $APP_ROOT/Gemfile
ADD ./Gemfile.lock $APP_ROOT/Gemfile.lock

RUN bundle install
ADD . $APP_ROOT