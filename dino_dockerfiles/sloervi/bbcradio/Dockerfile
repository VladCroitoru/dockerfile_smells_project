# Dockerfile sloervi/bbcradio
FROM sloervi/ubuntu-perl-music:v4
MAINTAINER sloervi McMurphy <docker@sloervi.de>

LABEL Description="Create Docker Image for downloading BBC Radio Shows with get_iplayer" Vendor="sloervi McMurphy" Version="1"

# Install get_iplayer
RUN mkdir -p /usr/local/bin && cd /usr/local/bin && git clone git://git.infradead.org/get_iplayer.git

# Get my scripts
RUN cd /usr/local/bin && git clone https://github.com/sloervi/bbcradio.git bbc

# Create User and group
RUN groupadd -r bbc && useradd -r -g bbc bbc
RUN chown -R bbc /usr/local/bin/bbc
RUN chmod u+x /usr/local/bin/bbc/bbc.sh
RUN chmod u+x /usr/local/bin/bbc/bbc.pl
RUN chown -R bbc /usr/local/bin/get_iplayer

VOLUME /data
VOLUME /config

ENTRYPOINT /usr/local/bin/bbc/bbc.sh
