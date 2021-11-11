FROM phusion/passenger-full:0.9.18
MAINTAINER Mike Danko <mike@l4m3.com>
RUN apt-get update -qq && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
RUN rm -f /etc/nginx/sites-enabled/default
RUN rm -f /etc/service/nginx/down
ADD build/site.conf /etc/nginx/sites-enabled/default
RUN mkdir -p /home/app/an
WORKDIR /home/app/an
ADD Gemfile Gemfile.lock /home/app/an/
RUN chown -R app:app /home/app/an
USER app
ENV HOME /home/app
RUN bundle install --deployment
ADD / /home/app/an/
USER root
ENV HOME /root
RUN chown -R app:app /home/app/an
ADD build/envs.conf /etc/nginx/main.d/envs.conf
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 80 443
