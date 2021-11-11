FROM octohost/ruby-2.1.2
MAINTAINER Josh Cox <josh 'at' webhosting.coop>

ENV HUBOARD_BASE_REFRESHED_AT 20141226

RUN apt-get update
RUN apt-get -y install nodejs supervisor
RUN apt-get -y install memcached couchdb redis-server ruby2.1-dev build-essential libssl-dev
RUN apt-get -y install libcurl4-openssl-dev libssl-dev libmagickcore-dev libmagickwand-dev libmysqlclient-dev libpq-dev libxslt1-dev libffi-dev libyaml-dev zlib1g-dev

ENV SEGMENTIO_KEY HUBOARD_SEGMENTIO_KEY
RUN git clone -b master https://github.com/rauhryan/huboard.git /app
#RUN cd /app; bundle install --deployment --without test development
#RUN cd /app; bundle install --deployment
RUN cd /app; sed -i 's/2.1.2/2.1.5/' Gemfile; rm Gemfile.lock
RUN cd /app; bundle install --no-deployment
RUN cd /app; bundle install --deployment --without test development

ADD supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf
ADD supervisor/couchdb.conf /etc/supervisor/conf.d/couchdb.conf
ADD supervisor/redis.conf /etc/supervisor/conf.d/redis.conf
ADD supervisor/foreman.conf /etc/supervisor/conf.d/foreman.conf
RUN sed -i 's/daemonize\ yes/daemonize\ no/' /etc/redis/redis.conf
RUN mkdir -p /var/run/couchdb
RUN chown -R couchdb. /var/run/couchdb

# Example usage in next layer
#ADD .env /app/.env
#RUN echo SESSION_SECRET=$(openssl rand -base64 32) >>/app/.env

#EXPOSE 5000
#EXPOSE 80
#EXPOSE 443

#CMD ["/usr/bin/supervisord"]
