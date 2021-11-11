# Copyright (C) 2017 Leandro Lisboa Penz <lpenz@lpenz.org>
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.

FROM debian:bullseye
MAINTAINER Leandro Lisboa Penz <lpenz@lpenz.org>

# install debian packages:
ENV DEBIAN_FRONTEND=noninteractive
RUN set -x -e; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        # shell:
        shellcheck \
        # yaml:
        python3-yaml \
        # python:
        flake8 \
        # perl
        libperl-critic-perl \
        # omnilint:
        python3-setuptools python3-pip python3-wheel python3-lxml \
        # base packages:
        locales gosu

# setup su and locale
RUN set -x -e; \
    sed -i '/pam_rootok.so$/aauth sufficient pam_permit.so' /etc/pam.d/su; \
    echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen; \
    locale-gen
ENV LC_ALL=en_US.UTF-8

# install pip packages:
RUN set -x -e; \
    pip install \
        ansible-lint==4.2.0

COPY container/omnilint-analyse /usr/local/bin/omnilint-analyse
COPY container/omnilint /usr/local/lib/python3.9/dist-packages/omnilint

# setup entrypoint with user UID/GID from host
RUN set -x -e; \
    (\
    echo '#!/bin/bash'; \
    echo 'set -e'; \
    echo 'if [ -z "$MY_UID" ]; then exec "${@:-/bin/bash}"; fi'; \
    echo 'MY_UID=${MY_UID:-1000}'; \
    echo 'useradd -M -u "$MY_UID" -o user'; \
    echo 'if [ -n "$RWD" ]; then cd "$RWD"; fi'; \
    echo 'exec gosu user "${@:-/bin/bash}"'; \
    ) > /usr/local/bin/entrypoint; \
    chmod a+x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]

CMD ["omnilint-analyse"]

# Run the container as:
# docker run -it --rm -u $UID -v $PWD:$PWD -w $PWD omnilint
