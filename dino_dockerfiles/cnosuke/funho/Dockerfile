FROM cnosuke/ruby23-base
MAINTAINER shinnosuke@gmail.com

RUN apt-get update
RUN apt-get install -y nginx mysql-client libmysqlclient-dev

# Add nginx configs and tricking logger to STDIO
COPY docker/nginx.conf /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /app /data /app/log /app/tmp
COPY Gemfile Gemfile.lock /app/
RUN cd /app && bundle install --without development test --deployment --quiet

WORKDIR /app
COPY . /app/

COPY .git/logs/HEAD /GIT_LOGS
RUN tail -1 /GIT_LOGS |awk '{print $2}' > /app/REVISION

RUN touch /app/.env

RUN bundle exec rake assets:precompile

COPY docker/Procfile /app/

EXPOSE 80
CMD ["bundle", "exec", "foreman", "start"]

# How to DB migrate
# docker-compose run -e RAILS_ENV=production --rm funho bundle exec rake ridgepole:apply
