FROM registry.gitlab.com/notch8/dev-ops/samvera:latest

COPY ops/nginx.sh /etc/service/nginx/run
COPY ops/webapp.conf /etc/nginx/sites-enabled/webapp.conf
COPY ops/env.conf /etc/nginx/main.d/env.conf

RUN gem install bundler -v 2.1.4
COPY --chown=app:app Gemfile* $APP_HOME/
RUN /sbin/setuser app bash -l -c "bundle check || bundle install"

COPY --chown=app:app . $APP_HOME
RUN /sbin/setuser app bash -l -c " \
    cd /home/app/webapp && \
    DB_ADAPTER=nulldb bundle exec rake assets:precompile && \
    mv ./public/assets ./public/assets-new"

CMD ["/sbin/my_init"]
