FROM postgres:9.5

RUN apt-get update &&\
    apt-get install -y curl daemontools gcc lzop pv python2.7-dev &&\
    rm -rf /var/lib/apt/lists/* &&\
    curl https://bootstrap.pypa.io/get-pip.py | python &&\
    pip install --no-cache-dir wal-e
