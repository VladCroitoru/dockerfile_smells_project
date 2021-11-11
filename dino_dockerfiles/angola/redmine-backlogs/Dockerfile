FROM sameersbn/redmine:3.2.4
MAINTAINER Angola

ENV REDMINE_VERSION=3.2.4 \
    REDMINE_USER="redmine" \
    REDMINE_HOME="/home/redmine" \
    REDMINE_LOG_DIR="/var/log/redmine" \
    REDMINE_CACHE_DIR="/etc/docker-redmine" \
    RAILS_ENV=production

ENV REDMINE_INSTALL_DIR="${REDMINE_HOME}/redmine" \
    REDMINE_DATA_DIR="${REDMINE_HOME}/data" \
    REDMINE_BUILD_DIR="${REDMINE_CACHE_DIR}/build" \
    REDMINE_RUNTIME_DIR="${REDMINE_CACHE_DIR}/runtime"


# プラグイン: redmine_backlogs
RUN git clone -b feature/redmine3 https://github.com/backlogs/redmine_backlogs.git plugins/redmine_backlogs
RUN sed -i -e "/gem \"nokogiri\"/d" -e "/gem \"capybara\"/d" plugins/redmine_backlogs/Gemfile
# プラグイン: redmine_slack
RUN git clone https://github.com/sciyoshi/redmine-slack.git plugins/redmine_slack

RUN bundle install --without development test
RUN RAILS_ENV=production && export RAILS_ENV

# テーマ: gitmake
RUN git clone git://github.com/makotokw/redmine-theme-gitmike.git ./public/themes/gitmike

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["app:start"]
