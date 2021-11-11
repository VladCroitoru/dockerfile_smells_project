FROM registry.gitlab.com/notch8/cal-state-hyrax/base:latest

ADD http://timejson.herokuapp.com build-time
#ADD ops/webapp.conf /etc/nginx/sites-enabled/webapp.conf
#ADD ops/env.conf /etc/nginx/main.d/env.conf
ADD . $APP_HOME

RUN cd /home/app/webapp && \
    (/sbin/setuser app bundle check || /sbin/setuser app bundle install) && \
    /sbin/setuser app bundle exec rake assets:precompile DB_ADAPTER=nulldb && \
    chown -R app $APP_HOME && \
    rm -f /etc/service/nginx/down

CMD ["/sbin/my_init"]

