FROM php:7.2.6-apache as builder

RUN apt-get update -y && \
    apt-get install -y build-essential \
                       nodejs \
                       ruby-full \
                       gnupg

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y npm

RUN gem install --no-rdoc --no-ri sass -v 3.4.22 && \
    gem install --no-rdoc --no-ri compass

RUN npm install -g grunt-cli

COPY . /var/www/html/
WORKDIR /var/www/html/

RUN npm install

RUN grunt

FROM php:7.2.6-apache

RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load

COPY --from=builder /var/www/html/ /var/www/html/
