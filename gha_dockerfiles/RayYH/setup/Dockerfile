# Based on https://github.com/Bash-it/bash-it-docker/blob/master/Dockerfile
FROM bash:5

ENV VERSION 0.0.1

# Optional Configuration Parameter
ARG SYSTEM_TZ

# Default Settings (for optional Parameter)
ENV SYSTEM_TZ ${SYSTEM_TZ:-Asia/Shanghai}

ENV SERVICE_USER set-up
ENV SERVICE_HOME /home/${SERVICE_USER}

RUN \
    adduser -h ${SERVICE_HOME} -s /bin/bash -u 1000 -D ${SERVICE_USER} && \
    apk add --no-cache \
    bash-completion \
    dumb-init \
    git \
    tzdata && \
    cp /usr/share/zoneinfo/${SYSTEM_TZ} /etc/localtime && \
    echo "${SYSTEM_TZ}" > /etc/TZ && \
    git clone --depth 1 https://github.com/rayyh/setup.git /tmp/setup && \
    cd /tmp/setup && \
    git pull origin master && \
    cp -R /tmp/setup /root/.setup && \
    cp -R /tmp/setup ${SERVICE_HOME}/.setup && \
    cp ${SERVICE_HOME}/.setup/.setuprc ${SERVICE_HOME}/.setuprc && \
    cp ${SERVICE_HOME}/.setup/.setuprc /root/.setuprc && \
    chown -R ${SERVICE_USER}:${SERVICE_USER} ${SERVICE_HOME} && \
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd && \
    apk del git tzdata && \
    rm -rf /tmp/{.}* /tmp/*

USER ${SERVICE_USER}

WORKDIR ${SERVICE_HOME}

RUN \
    echo 'test -e "${HOME}/.setup/setup.bash" && source "${HOME}/.setup/setup.bash"' >> ${SERVICE_HOME}/.bashrc && \
    echo 'alias reload="exec $SHELL"' >> ${SERVICE_HOME}/.bashrc && \
    /bin/bash "${SERVICE_HOME}/.bashrc"

ENTRYPOINT [ "/usr/bin/dumb-init", "bash" ]
