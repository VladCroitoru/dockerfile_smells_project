FROM ruby:2.3

ENV APP_NAME=brimir
ENV GIT_REPO="https://github.com/ivaldi/brimir"

ENV RAILS_ENV=production
ENV APP_HOME=/opt/${APP_NAME}
ENV SECRET_KEY_BASE="change_it_please"
ENV RAILS_LOG=${APP_HOME}/log/${RAILS_ENV}.log

ENV UNICORN_APP_NAME=unicorn_${APP_NAME}
ENV UNICORN_CONFIG=${APP_HOME}/config/${UNICORN_APP_NAME}.rb
ENV UNICORN_LOG_DIR=/var/log/unicorn
ENV UNICORN_LOG=${UNICORN_LOG_DIR}/${APP_NAME}.stdout.log
ENV UNICORN_ERROR_LOG=${UNICORN_LOG_DIR}/${APP_NAME}.stderr.log"
ENV UNICORN_PID=/var/run/${UNICORN_APP_NAME}.pid
ENV UNICORN_SOCK=/var/run/${UNICORN_APP_NAME}.sock
ENV UNICORN_WORKERS=2
ENV UNICORN_TIMEOUT=30
ENV UNICORN_PORT=3000

RUN apt-get update && apt-get install -y nodejs
RUN rm -r /var/lib/apt/lists/*

RUN mkdir -p ${APP_HOME}
RUN mkdir -p ${UNICORN_LOG_DIR}
WORKDIR ${APP_HOME}

RUN git clone ${GIT_REPO} ${APP_HOME}
RUN echo "gem 'unicorn'" >> Gemfile
COPY config/database.yml ${APP_HOME}/config/database.yml

RUN bundle install
RUN bundle exec rake assets:precompile

COPY config/unicorn.rb ${UNICORN_CONFIG}
COPY script/add_first_agent.rb ${APP_HOME}/db/
COPY config/action_mailer.rb ${APP_HOME}/config/initializers/action_mailer.rb

COPY script/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 700 /docker-entrypoint.sh

EXPOSE 3000
ENTRYPOINT ["/docker-entrypoint.sh"]
