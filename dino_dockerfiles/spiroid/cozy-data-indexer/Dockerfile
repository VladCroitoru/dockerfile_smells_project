FROM debian:sid
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray <jonathan.dray@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install --quiet --assume-yes --no-install-recommends \
    g++ \
    python \
    imagemagick \
    python-pip \
    python-virtualenv \
    virtualenv \
    python-dev \
    libxml2-dev \
    libxslt1-dev \
    python-setuptools \
    python-software-properties \
    software-properties-common \
    git \
    && apt-get clean

# Clean APT cache for a lighter image
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create Cozy users, without home directories.
RUN useradd -M cozy

#Host where dataindexer listen
ENV HOST dataindexer

RUN mkdir -p /usr/local/cozy-indexer \
&& cd /usr/local/cozy-indexer \
&& git clone --branch v1.0.6 --single-branch https://github.com/cozy/cozy-data-indexer.git \
&& cd /usr/local/cozy-indexer/cozy-data-indexer \
&& virtualenv --quiet /usr/local/cozy-indexer/cozy-data-indexer/virtualenv \
&& . ./virtualenv/bin/activate \
&& pip install -r /usr/local/cozy-indexer/cozy-data-indexer/requirements/common.txt \
&& chown -R cozy:cozy /usr/local/cozy-indexer

# Exposing ports
EXPOSE 9102

# Volumes configuration
VOLUME ["/usr/local/cozy-indexer/cozy-data-indexer"]

# Setting config dir to couch main directory
WORKDIR /usr/local/cozy-indexer/cozy-data-indexer

# Default user when running the container
USER cozy

CMD [ "./virtualenv/bin/python", "server.py" ]
