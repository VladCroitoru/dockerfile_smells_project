FROM ubuntu:xenial

MAINTAINER Raymond Tiefengraber

# Install apt packages
RUN apt-get update \
    && apt-get install -y python-pip \

# Clean downloaded apt packages after install
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

# Install python packages
    && pip install  'sphinx              == 1.6.2' \
                    'sphinx-autobuild    == 0.6.0' \
                    'sphinx_rtd_theme    == 0.2.4'

# Set the locale
ENV   LANG C.UTF-8
ENV   LANGUAGE C.UTF-8
ENV   LC_ALL C.UTF-8

# Expose sphinx-autobuild documentation served port
EXPOSE 8000

VOLUME  /sphinx-doc

# Set runtime command to autobuild and serve documentation
WORKDIR /sphinx-doc
CMD sphinx-autobuild -b html --host 0.0.0.0 --port 8000 --poll /sphinx-doc /sphinx-doc/_build/html
