FROM debian:jessie

CMD ["bash", "-c", "sleep 60; cd /data && source /synapse/bin/activate && synctl start; while ls /data/homeserver.pid &>/dev/null; do sleep 10; done"]

EXPOSE 8448

VOLUME ["/data"]

RUN set -ex export DEBIAN_FRONTEND=noninteractive ; \
    apt-get update; \
    apt-get install -y build-essential python2.7-dev libffi-dev \
                       python-pip python-setuptools sqlite3 \
                       libssl-dev python-virtualenv libjpeg-dev libxslt1-dev ; \
    virtualenv -p python2.7 /synapse; \
    bash -c 'source /synapse/bin/activate; pip install --upgrade pip; pip install --upgrade setuptools; pip install lxml; pip install https://github.com/matrix-org/synapse/tarball/master';



