FROM nebo15/alpine-erlang:latest
MAINTAINER Nebo#15 <support@nebo15.com>

# Install various tools
RUN apk --no-cache add xz curl jq su-exec bash && \
    rm -rf /var/cache/apk/*

# Install GOSU
ENV GOSU_VERSION 1.10
RUN set -x \
    && apk add --no-cache --virtual .gosu-deps \
        dpkg \
        gnupg \
        openssl \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apk del .gosu-deps

# Install additional Erlang modules
RUN apk --no-cache add erlang-hipe erlang-os-mon erlang-xmerl erlang-eldap

# Configure RabbitMQ
ENV RABBITMQ_VERSION=3.6.9 \
    RABBITMQ_USER=rabbitmq \
    RABBITMQ_HOME=/var/lib/rabbitmq \
    RABBITMQ_CONFIG_BASE=/etc/rabbitmq \
    RABBITMQ_LOG_BASE=/var/log/rabbitmq \
    RABBITMQ_INSTALL=/usr/lib/rabbitmq \
    RABBITMQ_SERVER_ERL_ARGS="+K true +A128 +P 1048576 -kernel inet_default_connect_options [{nodelay,true}]" \
    AUTOCLUSTER_VERSION=0.6.1 \
    ERL_EPMD_PORT=4369 \
    RABBITMQ_DIST_PORT=25672 \
    RABBITMQ_LOGS=- \
    RABBITMQ_SASL_LOGS=-

# Install RabbitMQ
RUN curl -sL "https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz" \
    | tar -xJ -C /tmp/ && \
    mv /tmp/rabbitmq_server-${RABBITMQ_VERSION} ${RABBITMQ_INSTALL}

# Install autocluster plugin
RUN curl -sL "https://github.com/aweber/rabbitmq-autocluster/releases/download/${AUTOCLUSTER_VERSION}/autocluster-${AUTOCLUSTER_VERSION}.tgz" \
    | tar -xz -C ${RABBITMQ_INSTALL}

# Set home so that any `--user` knows where to put the erlang cookie
ENV HOME $RABBITMQ_HOME

# /usr/sbin/rabbitmq-server has some irritating behavior, and only exists to "su - rabbitmq /usr/lib/rabbitmq/bin/rabbitmq-server ..."
ENV PATH ${RABBITMQ_INSTALL}/sbin:$PATH

# Set RabbitMQ paths
ENV RABBITMQ_CONFIG_FILE=${RABBITMQ_CONFIG_BASE}/rabbitmq \
    RABBITMQ_MNESIA_BASE=${RABBITMQ_HOME}/mnesia \
    RABBITMQ_ENABLED_PLUGINS_FILE=${RABBITMQ_CONFIG_BASE}/enabled_plugins \
    RABBITMQ_PLUGINS_DIR=${RABBITMQ_INSTALL}/plugins

# Create user and allow access to all necessary paths
RUN adduser -D -s /bin/sh ${RABBITMQ_USER} && \
    mkdir -p ${RABBITMQ_HOME} ${RABBITMQ_CONFIG_BASE} ${RABBITMQ_LOG_BASE} && \
    chown -R ${RABBITMQ_USER}: ${RABBITMQ_INSTALL} ${RABBITMQ_HOME} ${RABBITMQ_CONFIG_BASE} ${RABBITMQ_LOG_BASE} && \
    chmod -R 777 ${RABBITMQ_HOME} ${RABBITMQ_CONFIG_BASE} ${RABBITMQ_LOG_BASE}

# Performance tuning
RUN echo "net.core.somaxconn = 3072" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_max_syn_backlog = 4096" >> /etc/sysctl.conf && \
    echo "net.ipv4.conf.default.rp_filter = 0" >> /etc/sysctl.conf && \
    echo "fs.file-max = 2097152" >> /etc/sysctl.conf

# Allow all connections
RUN echo "${RABBITMQ_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR ${RABBITMQ_HOME}

# Enable sentitel plugins
RUN rabbitmq-plugins enable --offline \
        autocluster \
        rabbitmq_management_agent \
        rabbitmq_consistent_hash_exchange \
        rabbitmq_shovel && \
  rabbitmq-plugins list

        # rabbitmq_sharding \
        # rabbitmq_federation \

# Expose ports
EXPOSE 5671 5672 $RABBITMQ_DIST_PORT $ERL_EPMD_PORT

# Entrypoint from official Docker repo
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]

# Define default command
CMD ["rabbitmq-server"]
