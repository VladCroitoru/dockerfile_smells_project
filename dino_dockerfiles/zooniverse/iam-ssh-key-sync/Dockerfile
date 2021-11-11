FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
        jshon \
        python \
        python-pip \
        && \
    rm -rf /var/lib/apt/lists/*

RUN pip install awscli

COPY fetch_keys.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/fetch_keys.sh"]
