FROM phusion/passenger-ruby24:0.9.28

CMD ["/sbin/my_init"]

RUN rm /etc/nginx/sites-enabled/default

COPY config/nginx_docker/catchall_vhost.conf config/nginx_docker/main_vhost.conf /etc/nginx/sites-enabled/

RUN rm -f /etc/service/nginx/down

USER app

COPY config/nginx_docker/index_catchall.html /home/app/config/nginx_docker/public/404.html

WORKDIR /home/app/

COPY Gemfile Gemfile.lock ./

USER root

RUN bundle --without development test --jobs 4

USER app

COPY . /home/app/

USER root

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
