FROM ubuntu
MAINTAINER wailorman

RUN apt-get update && \
    apt-get install npm nodejs-legacy git git-core -y

RUN mkdir /tmp/www && \
    mkdir /var/www

COPY . /tmp/www

WORKDIR /tmp/www

RUN npm install --unsafe-perm
RUN /usr/bin/node ./node_modules/bower/bin/bower install --allow-root
RUN /usr/bin/node ./node_modules/grunt-cli/bin/grunt

CMD cp -avr /tmp/www/built/* /var/www

VOLUME ["/var/www"]