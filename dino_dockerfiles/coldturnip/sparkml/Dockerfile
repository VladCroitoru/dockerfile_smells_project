FROM alpine:latest

# Build image:
#
#   $ docker build -t sparkml - < sparkml.dockerfile
#
# Image usage (mount scripts and sample data to container's /ml and /ml_data):
#
#   $ git clone https://github.com/sparktsao/HappyCat.git
#   $ docker run -v HappyCat/learning:/ml -v HappyCat/dataset/unittest:/ml_data \
#                --name happycat --rm -t -i sparkml python happycat.py /ml_data/ 2 unittest
#

# There are four steps to setup this environment; modify them to fit your need:
#   1. prepare system-wide settings, and install Python 2.x
#   2. install packages needed by PIP into virtual package "build-dependencies"
#   3. make symbolic links for Python
#   4. install Python 3rd-party packages
RUN echo '@testing http://dl-4.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk add --update musl 'python<3' && \
    apk add --virtual=build-dep \
            build-base \
            'python-dev<3' \
            py-pip && \
    apk add py-numpy-dev@testing && \
    ( cd /usr/bin ; \
      ln -sf easy_install-2.* easy_install ; \
      ln -sf $(ls | grep '^python2.[0-9]*$') python ; \
      ln -sf python2.*-config python-config ; \
      ln -sf pip2.* pip ; \
    ) ; \
    pip install --upgrade pip && \
    apk add py-numpy@testing py-scipy@testing && \
    pip install keras sklearn pandas && \
    apk del build-dep py-numpy-dev && \
    rm /var/cache/apk/*

ENV MLWORKPATH /ml
ENV MLDATAPATH /ml_data
VOLUME ["/ml", "/ml_data"]
WORKDIR $MLWORKPATH
CMD python
