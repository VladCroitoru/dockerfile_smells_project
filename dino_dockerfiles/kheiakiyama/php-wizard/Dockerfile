FROM isag17/docker-composer:latest

RUN apt-get update && apt-get install -y \
          vim \
          --no-install-recommends && rm -r /var/lib/apt/lists/*
RUN a2enmod rewrite

ENV APP_HOME /var/www/html

#copy project
COPY . $APP_HOME

RUN find $APP_HOME -type d -exec chmod 755 {} \;
RUN find $APP_HOME -type f -exec chmod 644 {} \;
