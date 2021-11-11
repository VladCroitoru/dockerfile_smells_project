FROM debian:jessie

# - download and install opentuner
RUN apt-get update && \
    apt-get install -y wget tar procps build-essential python-pip python-dev libsqlite3-dev sqlite3 lxc && \
    cd / && \
    wget --no-check-certificate https://github.com/jansel/opentuner/tarball/master -O - | tar xz && \
    mv jansel* opentuner && \
    cd /opentuner && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install -e .

ENV OPENTUNER_DIR /opentuner

# add our tuner
ADD torpor.py /usr/bin/

ENTRYPOINT ["/usr/bin/torpor.py"]
CMD ["--help"]
