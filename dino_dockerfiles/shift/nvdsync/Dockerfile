FROM shift/nvdxjira:latest

MAINTAINER Vincent Palmer <shift@someone.section.me>

WORKDIR /usr/local/src
RUN apt-get update \
    && apt-get install --yes git \
    && git clone https://github.com/shift/nvdsync.git \
    && cp nvdsync/src/nvdsync /usr/local/bin \
    && chmod 0755 /usr/local/bin/nvdsync \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/src/nvdsync \
    && cd \
    && apt-get purge --yes git
