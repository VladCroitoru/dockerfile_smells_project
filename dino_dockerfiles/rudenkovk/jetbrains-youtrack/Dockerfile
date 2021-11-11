FROM rudenkovk/java-docker

MAINTAINER "Konstantin Rudenkov" <rudenkovk@gmail.com>

ARG YOUTRACK_VERSION=7.0
ARG YOUTRACK_BUILD=28110

LABEL \
    version="$(YOUTRACK_VERSION}.${YOUTRACK_BUILD}" \
    ru.rudenkovk.jetbrains-hub-version="${YOUTRACK_VERSION}.${YOUTRACK_BUILD}" \
    ru.rudenkovk.vcs-url="https://github.com/rudenkovk/jetbrains-youtrack"

ENV APP_NAME=youtrack \
    APP_PORT=8080 \
    APP_UID=500 \
    APP_PREFIX=/opt

ENV APP_USER=$APP_NAME \
    APP_DIR=$APP_PREFIX/$APP_NAME \
    APP_HOME=/var/lib/$APP_NAME

# RUN useradd --system --user-group --uid $APP_UID --home $APP_HOME $APP_USER \
#     && mkdir $APP_HOME \
#     && chown -R $APP_USER:$APP_USER $APP_HOME

WORKDIR $APP_PREFIX

RUN wget -qO ${APP_NAME}.zip https://download.jetbrains.com/charisma/youtrack-${YOUTRACK_VERSION}.${YOUTRACK_BUILD}.zip && \
    unzip -q ${APP_NAME}.zip -x */internal/java/* && \
    mv youtrack-${YOUTRACK_BUILD} $APP_NAME && \
    # chown -R $APP_USER:$APP_USER $APP_DIR && \
    rm ${APP_NAME}.zip

# USER $APP_USER
WORKDIR $APP_DIR

RUN bin/youtrack.sh configure \
    --backups-dir $APP_HOME/backups \
    --data-dir    $APP_HOME/data \
    --logs-dir    $APP_HOME/log \
    --temp-dir    $APP_HOME/tmp \
    --listen-port $APP_PORT \
    --base-url    http://localhost/

EXPOSE $APP_PORT
VOLUME ["$APP_HOME"]
ENTRYPOINT ["bin/youtrack.sh"]
CMD ["run"]
