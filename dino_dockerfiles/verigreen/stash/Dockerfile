FROM atlassian/stash:3.8
MAINTAINER Giovanni Matos http://github.com/gmatoshp

ENV RUN_USER=root  \
    RUN_GROUP=root \
    STASH_PORT=7990 \
    STASH_GIT_PORT=7999 \
    STASH_CONFIG_PATH=/var/stash/config \
    STASH_HOST=localhost

USER root

# Installing required packages
# Requires Python (with requests and yaml) for automatic setup and sendmail for sending mail
RUN apt-get update -qq   \
    && apt-get install -y --no-install-recommends \
    #sendmail                                     \
    python python-requests python-yaml            \
    python-pygresql python-setuptools             \
    libaio1                                       \
    python-dev python-pip build-essential         \
    libpq-dev                                     \
    && apt-get clean autoclean                    \
    && apt-get autoremove --yes                   \
    && rm -rf                  /var/lib/{apt,dpkg,cache,log}/


# HTTP Port 7990 exposed in base image
# SSH Port  7999 exposed in base image

# Create directories for volume mounting and defaults
RUN mkdir -p /var/stash/plugins && mkdir -p /var/stash/config 

ADD run.sh run.sh
ADD stash_setup.py stash_setup.py
ADD checkdb.py checkdb.py
# Run setup script
CMD ./run.sh  $STASH_INSTALL_DIR
