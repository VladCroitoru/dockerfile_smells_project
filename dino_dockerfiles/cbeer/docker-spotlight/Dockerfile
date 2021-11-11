FROM phusion/passenger-ruby22

ENV HOME /home/app/webapp
ENV BLACKLIGHT_INSTALL_OPTIONS "--devise"
RUN gem install rails && rails new /home/app/webapp --database postgresql -q -m https://raw.githubusercontent.com/sul-dlss/spotlight/master/template.rb

WORKDIR /home/app/webapp

RUN SECRET_KEY_BASE=x rake assets:precompile
RUN chown app -R /home/app/webapp

# we'll provide the DATABASE_URL in the env
RUN rm -f /home/app/webapp/config/database.yml

RUN rm -f /etc/service/nginx/down
RUN rm /etc/nginx/sites-enabled/default

ADD webapp.conf /etc/nginx/sites-enabled/default
ADD rails-env.conf /etc/nginx/main.d/rails-env.conf
ADD blacklight-env.conf /etc/nginx/main.d/blacklight-env.conf
ADD client_max_body_size.conf /etc/nginx/conf.d/client_max_body_size.conf

RUN mkdir -p /etc/my_init.d
ADD bootstrap-solr.sh /etc/my_init.d/bootstrap-solr.sh
RUN chmod o+x /etc/my_init.d/bootstrap-solr.sh

ADD bootstrap-db.sh /etc/my_init.d/bootstrap-db.sh
RUN chmod o+x /etc/my_init.d/bootstrap-db.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]
