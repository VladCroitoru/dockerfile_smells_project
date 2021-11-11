FROM ruby:3.0.2

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get update -qq && \
    apt-get install -y build-essential \ 
                       libpq-dev \
                       vim \
                       yarn \
                       nodejs 

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /communiteer
ENV APP_ROOT /communiteer
WORKDIR $APP_ROOT

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

ADD ./Gemfile $APP_ROOT/Gemfile
ADD ./Gemfile.lock $APP_ROOT/Gemfile.lock

RUN gem install bundler 
RUN bundle install
ADD . $APP_ROOT
