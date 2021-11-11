# /path/to/app/Dockerfile
FROM ruby:2.7.3

# Соберем все во временной директории
WORKDIR /tmp
ADD Gemfile* ./
RUN git config --global http.sslverify false

RUN bundle install
# Копирование кода приложения в контейнер
ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

# Настройка переменных окружения для production
ENV RAILS_ENV=production

# Проброс порта 5000
EXPOSE 5000

# Запуск по умолчанию сервера puma
CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]

