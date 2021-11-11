FROM ruby:2.3

# install nodejs runtime
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

# install app
COPY . /usr/src/walklc
WORKDIR /usr/src/walklc
RUN bundle install

# configure app
ENV RAILS_ENV production
ENV DB_HOST db

# run
EXPOSE 3000
CMD ["rails", "s", "-b", "0.0.0.0"]
