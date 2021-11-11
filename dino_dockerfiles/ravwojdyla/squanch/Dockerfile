FROM google/cloud-sdk
MAINTAINER Rafal Wojdyla <rav@spotify.com>

RUN apt-get update -qq  \
    && apt-get install --no-install-recommends -yy -qq \
      jq \
      python-pip \
    && echo "\n\nDeb requirements installed\n\n" \
    && apt-get clean -qq \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pyyaml

COPY ["bin", "/squanch/bin"]
COPY ["conf", "/squanch/conf"]

WORKDIR /squanch
VOLUME ["/etc/jmxtrans"]

ENV TERM xterm
ENV PROBE_INTERVAL 60
ENV JOB_ID ""

ENTRYPOINT ["/bin/sh", "-c", \
            "while true; do ./bin/gen_jmxtrans_at_change.sh /etc/jmxtrans $JOB_ID; sleep $PROBE_INTERVAL; done"]
