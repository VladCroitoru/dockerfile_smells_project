FROM rudenkovk/java-docker

MAINTAINER "Konstantin Rudenkov" <rudenkovk@gmail.com>

ARG HUB_VERSION=2.5
ARG HUB_BUILD=399

LABEL \
    version="${HUB_VERSION}.${HUB_BUILD}" \
    ru.rudenkovk.jetbrains-hub-version="${HUB_VERSION}.${HUB_BUILD}" \
    ru.rudenkovk.vcs-url="https://github.com/rudenkovk/jetbrains-hub"

ENV APP_NAME=hub \
    APP_PORT=8080 \
    APP_UID=500 \
    APP_PREFIX=/srv \
    APP_DISTNAME="hub-ring-bundle-${HUB_VERSION}.${HUB_BUILD}"

ENV APP_USER=$APP_NAME \
    APP_DIR=$APP_PREFIX/$APP_NAME \
    APP_HOME=/var/lib/$APP_NAME \
    APP_DISTFILE="${APP_DISTNAME}.zip"

# RUN useradd --system --user-group --uid ${APP_UID} --home ${APP_HOME} ${APP_USER} \ 
#     && mkdir $APP_HOME \
#     && chown -R $APP_USER:$APP_USER $APP_HOME

RUN mkdir ${APP_HOME}

WORKDIR $APP_PREFIX

RUN wget -q https://download.jetbrains.com/hub/$HUB_VERSION/$APP_DISTFILE \
    && unzip -q $APP_DISTFILE -x */internal/java/* \
    && mv $APP_DISTNAME $APP_NAME \
    && rm $APP_DISTFILE
    # && chown -R $APP_USER:$APP_USER $APP_DIR 

# USER $APP_USER
WORKDIR $APP_DIR

RUN bin/hub.sh configure \
    --backups-dir $APP_HOME/backups \
    --data-dir    $APP_HOME/data \
    --logs-dir    $APP_HOME/log \
    --temp-dir    $APP_HOME/tmp \
    --listen-port $APP_PORT \
    --base-url    http://localhost/

ENTRYPOINT ["bin/hub.sh"]
CMD ["run"]
EXPOSE $APP_PORT
VOLUME ["$APP_HOME"]