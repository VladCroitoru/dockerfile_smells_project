FROM ubuntu:15.04

MAINTAINER Vincent Palmer <shift@someone.section.me>

WORKDIR /usr/local/src
RUN apt-get update \
    && apt-get install --yes git python make \
    && git clone https://github.com/shift/nvdXjira.git \
    && cd nvdXjira \
    && make install \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/src/nvdXjira \
    && cd \
    && apt-get purge --yes git make \
    && mkdir -p /etc/nvdXjira

ENTRYPOINT ["/usr/local/bin/nvdXjira"]
