FROM debian:jessie

RUN apt-get -qq update \
    && apt-get -qqy install \
    git \
    curl \
    make \
    golang \
    gcc \
    \
    && cd /root/ \
    && mkdir prometheus \
    && cd prometheus \
    && mkdir src \
    && cd src \
    && git clone https://github.com/prometheus/prometheus.git \
    && cd .. \
    && curl -sSL https://github.com/prometheus/prometheus/releases/download/0.15.0/prometheus-0.15.0.linux-amd64.tar.gz | tar zxfv - -C . \
    \
    && cd /root/ \
    && git clone https://github.com/prometheus/client_golang.git \
    && cd client_golang \
    && make example_random

COPY prometheus.yml /root/
COPY startup.sh /root/

RUN chmod a+x /root/startup.sh

CMD /root/startup.sh
