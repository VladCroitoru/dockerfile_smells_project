FROM debian:latest
MAINTAINER Rony Dray <contact@obigroup.fr>

RUN echo 'deb http://http.debian.net/debian wheezy main contrib non-free' >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get install -y \
    g++ \
    python \
    imagemagick \
    python-pip \
    python-dev \
    libxml2-dev \
    libxslt1-dev \
    python-setuptools \
    python-software-properties \
    software-properties-common \
    git \
    && apt-get clean

RUN pip install \
supervisor \
virtualenv

# Create Cozy users, without home directories.
RUN useradd -M cozy

#Host where dataindexer listen
ENV HOST dataindexer

RUN mkdir -p /usr/local/cozy-indexer \
&& cd /usr/local/cozy-indexer \
&& git clone https://github.com/cozy/cozy-data-indexer.git \
&& cd /usr/local/cozy-indexer/cozy-data-indexer \
&& virtualenv --quiet /usr/local/cozy-indexer/cozy-data-indexer/virtualenv \
&& . ./virtualenv/bin/activate \
&& pip install -r /usr/local/cozy-indexer/cozy-data-indexer/requirements/common.txt \
&& chown -R cozy:cozy /usr/local/cozy-indexer

# Clean APT cache for a lighter image
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configure Supervisor.
ADD supervisor/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/log/supervisor
RUN chmod 774 /var/log/supervisor
RUN /usr/local/bin/supervisord -c /etc/supervisord.conf

# Import Supervisor configuration files.
ADD supervisor/cozy-indexer.conf /etc/supervisor/conf.d/cozy-indexer.conf
RUN chmod 0644 /etc/supervisor/conf.d/*

# EXPOSE 9102

VOLUME ["/usr/local/cozy-indexer/cozy-data-indexer"]

CMD [ "/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf" ]