FROM phusion/passenger-ruby25:0.9.29

MAINTAINER Hidetoshi Yoshimoto hidetoshi.yoshimoto@gmail.com

# Passenger app container cannot read shell variables.
# It should be set by 'passenger_env_var' setting on nginx config.
# See nginx_webapp.conf
# This Dockerfile replace __VARS__ with Docker ARGs.
ARG LDAP_BASE_DN
ARG LDAP_BIND_DN
ARG LDAP_BIND_PASSWORD
ARG MYSQL_ROOT_PASSWORD
ARG IDP_HOST_NAME
ARG IDP_SCOPE
ARG JETTY_KEYSTORE_PASSWORD

# ARGs values copy to shell variables.
# rails command will use it.
ENV LDAP_BASE_DN $LDAP_BASE_DN
ENV LDAP_BIND_DN $LDAP_BIND_DN
ENV LDAP_BIND_PASSWORD $LDAP_BIND_PASSWORD
ENV MYSQL_ROOT_PASSWORD $MYSQL_ROOT_PASSWORD
ENV IDP_HOST_NAME $IDP_HOST_NAME
ENV IDP_SCOPE $IDP_SCOPE
ENV JETTY_KEYSTORE_PASSWORD $JETTY_KEYSTORE_PASSWORD

ENV APP_ROOT /home/app/ezidpums
WORKDIR $APP_ROOT

ENV HOME /root
CMD ["/sbin/my_init"]

RUN apt-get update && \
    apt-get install -y nodejs \
                       mysql-client \
                       postgresql-client \
                       sqlite3 \
                       ldap-utils \
                       libldap2-dev \
                       --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY Gemfile $APP_ROOT
COPY Gemfile.lock $APP_ROOT

# Default version of RubyGems(2.7.3) does not work with passenger! It should be update.
RUN \
  gem update --system && \
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc && \
  bundle config --global build.nokogiri --use-system-libraries && \
  bundle config --global jobs 4 && \
  bundle install && \
  rm -rf ~/.gem

RUN rm -f /etc/service/nginx/down
RUN rm /etc/nginx/sites-enabled/default
COPY . $APP_ROOT
RUN chown -R app.app $APP_ROOT
RUN sed -e "s/__secret_key_base__/`bundle exec rails secret`/" $APP_ROOT/nginx_webapp.conf > /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__ldap_base_dn__/$LDAP_BASE_DN/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__ldap_bind_dn__/$LDAP_BIND_DN/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__ldap_bind_password__/$LDAP_BIND_PASSWORD/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__mysql_root_password__/$MYSQL_ROOT_PASSWORD/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__idp_host_name__/$IDP_HOST_NAME/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__idp_socpe__/$IDP_SCOPE/" /etc/nginx/sites-enabled/webapp.conf && \
    sed -i -e "s/__jetty_keystore_password__/$JETTY_KEYSTORE_PASSWORD/" /etc/nginx/sites-enabled/webapp.conf
RUN bundle exec rails assets:precompile
