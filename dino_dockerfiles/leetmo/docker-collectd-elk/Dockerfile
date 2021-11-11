FROM python:2.7-slim

RUN ( \
    set -eux; \
    export DEBIAN_FRONTEND=noninteractive; \

    DOCKER_PLUGIN_URL=https://codeload.github.com/signalfx/docker-collectd-plugin/tar.gz/1e4ada70a52ca374b82d8c5222c8919c297e69fb; \

    # add jessie-backports for latest version of collectd
    echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list; \

    apt-get update; \
    apt-get install -y --no-install-recommends make curl; \
    apt-get install -t jessie-backports -y --no-install-recommends collectd collectd-core; \

    mkdir -p /usr/share/collectd/docker-collectd-plugin; \
    curl -s -o- $DOCKER_PLUGIN_URL | tar -xz --strip-components 1 -C /usr/share/collectd/docker-collectd-plugin -f-; \

    pip install -r /usr/share/collectd/docker-collectd-plugin/requirements.txt; \
)

COPY collectd.conf /etc/collectd/collectd.conf
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

