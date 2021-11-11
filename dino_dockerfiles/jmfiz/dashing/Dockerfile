FROM ubuntu:14.04
MAINTAINER jmfiz <jmfiz@paradigmatecnologico.com>

# update, upgrade and install requirements
RUN apt-get update -qq && \
    apt-get upgrade -qqy && \
    apt-get install -qqy \
    ruby1.9.1 \
    ruby1.9.1-dev \
    build-essential \
    nodejs \
    libcurl4-openssl-dev \
    supervisor && \
    gem install bundler && \
    gem install dashing && \
    gem install curb && \
    gem install xml-simple && \
    gem install net-http-persistent && \
    gem install rdoc

# create dashing dashboard
RUN mkdir /dashboard && \
    dashing new dashboard && \
    cd /dashboard && bundle install 

# dashboard setup
COPY dashboard /etc/init.d/dashboard
RUN chmod 755 /etc/init.d/dashboard && \
    update-rc.d dashboard defaults

# supervisor setup
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# configure environment
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/bundle:/usr/local/bundle/bin
ENV GEM_HOME /usr/local/bundle
RUN bundle config --global path "$GEM_HOME" \
    && bundle config --global bin "$GEM_HOME/bin"

WORKDIR /dashboard

VOLUME ["/dashboard"]

EXPOSE 3030

# Start dashing + supervisord
CMD ["supervisord","-c", "/etc/supervisor/supervisord.conf"]
