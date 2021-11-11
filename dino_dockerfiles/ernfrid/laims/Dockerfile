FROM ubuntu:16.04
LABEL maintainer "Dave Larson <delarson@wustl.edu>"
LABEL description="Lame analysis information management system"

COPY . /tmp/src

RUN apt-get update -qq \
    && apt-get -y install apt-transport-https \
    && apt-get update -qq \
    && apt-get -y install --no-install-recommends \
        libnss-sss \
        python \
        python-pip \
    && pip install --upgrade pip \
    && pip install setuptools wheel \
    && cd /tmp/src \
    && pip install --process-dependency-links . \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/src

CMD ["/bin/bash"]
