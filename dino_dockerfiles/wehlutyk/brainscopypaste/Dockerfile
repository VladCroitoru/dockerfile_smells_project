FROM ubuntu:16.04
MAINTAINER Sébastien Lerique <sl@mehho.net>

# Install all the system and build dependencies.
ENV PYTHON_VERSION 3.5
ENV PG_VERSION 9.5
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        libfreetype6-dev \
        libpng12-0 \
        libpng12-dev \
        locales \
        pkg-config \
        postgresql-${PG_VERSION} \
        postgresql-server-dev-${PG_VERSION} \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev \
        python3 \
        python3-pip \
        sudo \
        texlive \
        texlive-latex-extra \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Make the "en_US.UTF-8" locale so postgres and python Click will be utf-8
# enabled by default.
RUN set -x \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LC_ALL en_US.utf8
ENV LANG en_US.utf8

# Set up postgres with user and analysis and test databases for brainscopypaste.
RUN set -x \
    && service postgresql start \
    && sudo -u postgres psql -c 'create user brainscopypaste;' \
    && sudo -u postgres psql -c 'create database brainscopypaste;' \
    && sudo -u postgres psql -c 'alter database brainscopypaste owner to brainscopypaste;' \
    && sudo -u postgres psql -c 'create database brainscopypaste_test;' \
    && sudo -u postgres psql -c 'alter database brainscopypaste_test owner to brainscopypaste;' \
    && sed -i 's/^\(\(local\|host\) \+all \+all \+.* \+\)\(peer\|md5\)$/\1trust/g' /etc/postgresql/${PG_VERSION}/main/pg_hba.conf

# Copy the originating repository, and install requirements.
COPY . /home/brainscopypaste
RUN set -x \
    && cd /home/brainscopypaste \
    && pip3 install --upgrade pip setuptools \
    && pip install $(cat requirements.txt | grep "^numpy") \
    && pip install -r requirements.txt \
    && pip install --editable .

# Configure the brainscopypaste user.
RUN set -x \
    && useradd brainscopypaste \
    && echo "brainscopypaste ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/brainscopypaste \
    && chown -R brainscopypaste:brainscopypaste /home/brainscopypaste
USER brainscopypaste

# Install treetagger and datasets.
RUN set -x \
    && cd /home/brainscopypaste \
    && ./install_treetagger.sh \
    && ./install_datasets.sh

# Clean up to reduce image size.
RUN set -x \
    && sudo rm -rf /root/.cache/pip \
    && sudo apt-get purge -y --auto-remove \
        build-essential \
        ca-certificates \
        libfreetype6-dev \
        libpng12-dev \
        pkg-config \
        postgresql-server-dev-${PG_VERSION} \
        python${PYTHON_VERSION}-dev \
        python3-pip \
        unzip \
        wget

# Check the software runs its tests.
RUN set -x \
    && cd /home/brainscopypaste \
    && sudo service postgresql restart \
    && py.test
