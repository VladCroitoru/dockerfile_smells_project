FROM bbugyi/python:2021.09.25

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG USER_ID
ARG GROUP_ID

### install dpkgs
COPY dpkg-dependencies.txt /tmp/
# hadolint ignore=SC2046
RUN apt-get install -y --no-install-recommends --allow-unauthenticated $(grep "^[A-Za-z]" /tmp/dpkg-dependencies.txt | perl -nE 'print s/^([^#]+)[ ]+#.*/\1/gr') && \
    apt-get clean

### create new user account ('docker')
RUN groupadd --gid $GROUP_ID docker && \
        useradd --no-log-init --create-home --uid $USER_ID --gid docker docker && \
        cp /bashrc /home/docker/.bashrc
USER docker
