FROM phusion/passenger-ruby23

MAINTAINER Hunter Long <info@socialeck.com>
#
# === Phusion Nginx Web Server running Ruby on Rails
#
# docker run -d -p 80:80 -e 'GIT_REPO=railsapps/learn-rails' hunterlong/auto-phusion-rails
#
#   - Go Production mode with  -e 'RAILS_ENV=production'
#   - You can mount installed gems '-v /my/local/gems:/usr/local/gems' for fast startup
#   - Automatically pulls from Github and runs app.
#

# Standard ENVs
ENV HOME /root
ENV RAILS_ENV development
ENV PASSENGER_APP_ENV $RAILS_ENV
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH

# Env Vars for Github
ENV GIT_EMAIL $GIT_EMAIL
ENV GIT_NAME $GIT_NAME
ENV GIT_REPO $GIT_REPO
ENV GIT_BRANCH master
ENV GIT_USERNAME $GIT_USERNAME
ENV GIT_PERSONAL_TOKEN $GIT_PERSONAL_TOKEN

RUN rm -f /etc/service/nginx/down

ADD scripts/start.sh /root/start.sh
RUN chmod 777 /root/start.sh

RUN rm /etc/nginx/sites-enabled/default

ADD conf/nginx/rails_env.conf /etc/nginx/main.d/rails_env.conf
ADD conf/nginx/app.conf /etc/nginx/sites-enabled/webapp.conf

WORKDIR /var/www/html

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["/root/start.sh"]
