FROM ruby:3.0.0

WORKDIR /app

COPY Gemfile /app/Gemfile
COPY app.rb /app/app.rb
COPY config.ru /app/config.ru
COPY helper/request-helper.rb /app/helper/request-helper.rb
COPY helper/custom_controller.rb /app/helper/custom_controller.rb
COPY helper/custom_exporter.rb /app/helper/custom_exporter.rb

EXPOSE 8080
RUN gem install bundler
RUN bundle install
CMD ["bundle", "exec", "rackup", "config.ru", "-o", "0.0.0.0", "-p", "8080"]