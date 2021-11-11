FROM webdevops/php-apache:7.1

WORKDIR /root
RUN apt-get update -y && curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs && npm install npm -g
WORKDIR /app
