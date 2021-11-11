
FROM aslittledesign/portfolio-base-image
MAINTAINER "Dave Scott McCarthy <dave@aslittledesign.com>"

# Set up app
WORKDIR /tmp
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock

RUN bundle install --jobs 20 --retry 5

# Set up NGINX
ADD container/nginx_signing.key /var/www/nginx_signing.key
RUN apt-key add /var/www/nginx_signing.key
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y nginx

RUN mkdir -p /run/nginx
RUN rm -rf /etc/nginx/sites-available/default
ADD container/nginx.conf /etc/nginx/nginx.conf

ENV APP_HOME /portfolio-neue
RUN mkdir -p $APP_HOME
ADD . $APP_HOME
WORKDIR $APP_HOME

# Set up ENV variables
RUN touch .env
RUN echo "SECRET_KEY_BASE=$(bundle exec rake secret)" >> .env
RUN echo "SECRET_TOKEN=$(bundle exec rake secret)" >> .env

RUN RAILS_ENV=production bundle exec rake assets:precompile --trace

EXPOSE 80
EXPOSE 443

CMD ["foreman","start"]
