FROM ubuntu:latest

LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>

#################
#### curl/wget
#################
RUN apt-get update && apt-get install curl wget -y

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && apt-get install -y --allow-unauthenticated \
    supervisor \
    build-essential \
    git \
    libzmq3-dev \
    module-init-tools \
    pkg-config \
    python \
    python-dev \
    python3 \
    rsync \
    software-properties-common \
    unzip \
    zip \
    zlib1g-dev \
    vim \
    python-pip \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip3 install --upgrade pip

##############################
# Python 2 packages
##############################

RUN pip2 --no-cache-dir install elasticsearch requests stomp.py

#############################
# Python 3 packages
#############################

RUN pip3 --no-cache-dir install elasticsearch requests stomp.py

ADD tools.py /.
ADD siteMapping.py /.
ADD NetworkLatencyCollector.py /.
ADD NetworkLHCOPNCollector.py /.
ADD NetworkMLTelemetryCollector.py /.
ADD NetworkPacketLossCollector.py /.
ADD NetworkRetransmitsCollector.py /.
ADD NetworkThroughputCollector.py /.
ADD NetworkTracerouteCollector.py /.
ADD NetworkMetaCollector.py /.
ADD NetworkStatusCollector.py /.

# setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY supervisord.cern.conf /etc/supervisor/conf.d/supervisord.cern.conf

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]
