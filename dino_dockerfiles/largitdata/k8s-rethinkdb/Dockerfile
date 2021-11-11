FROM rethinkdb:2.3.5

MAINTAINER Brian Luan <jznight@gmail.com>

RUN apt-get update && \
    apt-get install -yq curl && \
    apt-get install -yq python-pip && \
    pip install rethinkdb && \
    rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*


ADD http://stedolan.github.io/jq/download/linux64/jq /usr/bin/jq
RUN chmod +x /usr/bin/jq

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

COPY ./run.sh ./probe.py ./ready-probe.py /
RUN chmod u+x /run.sh /probe.py /ready-probe.py

ENTRYPOINT ["/usr/local/bin/dumb-init", "/run.sh"]
