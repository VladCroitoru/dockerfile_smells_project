FROM octohost/middleman-nginx

WORKDIR /srv/www
ADD . /srv/www/
RUN bundle install
RUN bundle exec middleman build

EXPOSE 80

CMD nginx
