FROM phusion/passenger-ruby24

ENV HOME /root
ENV RAILS_ENV production

CMD ["/sbin/my_init"]
RUN rm -f /etc/service/nginx/down
RUN gem update --system
RUN rm /etc/nginx/sites-enabled/default
ADD config/webapp.conf /etc/nginx/sites-enabled/webapp.conf
RUN mkdir /home/app/darkroom
ADD config/postgres-env.conf /etc/nginx/main.d/postgres-env.conf
ADD . /home/app/darkroom
WORKDIR /home/app/darkroom
RUN bundle install
RUN rake assets:precompile
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 80