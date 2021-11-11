FROM eclipse/stack-base:ubuntu

ENV DOCKER_VERSION=17.09.1 \
    UNISON=/projects/.unison \
    UNISONLOCALHOSTNAME=che-server

USER root

RUN apt-get update && apt-get install -y --no-install-recommends curl wget make nano netcat jq mysql-client openssh-server unison && \
    curl -L -o /usr/local/bin/unison-fsmonitor https://github.com/TentativeConvert/Syndicator/raw/master/unison-binaries/unison-fsmonitor && \
    chmod +x /usr/local/bin/unison-fsmonitor && \
    wget -qO- https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}-ce.tgz | tar zxf - --strip=1 -C /usr/local/bin/ && \
    mkdir -p /home/user/.ssh && chown user:user /home/user/.ssh && \
    echo 'GatewayPorts yes' >> /etc/ssh/sshd_config

COPY edge.sh /home/user/

RUN wget -qO- https://raw.githubusercontent.com/outeredge/dredger/master/install.sh | bash

USER user

CMD /home/user/edge.sh && tail -f /dev/null
