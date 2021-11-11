# Copyright (c) 2021 , Veepee
#
# Permission  to use,  copy, modify,  and/or distribute  this software  for any
# purpose  with or  without  fee is  hereby granted,  provided  that the  above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS  SOFTWARE INCLUDING ALL IMPLIED  WARRANTIES OF MERCHANTABILITY
# AND FITNESS.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL  DAMAGES OR ANY DAMAGES  WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER  TORTIOUS ACTION,  ARISING OUT  OF  OR IN  CONNECTION WITH  THE USE  OR
# PERFORMANCE OF THIS SOFTWARE.

FROM docker.registry.vptech.eu/vptech/debian:latest

ARG NOMAD_VERSION="1.0.4"

ENV NOMAD_RELEASE="https://releases.hashicorp.com/nomad/$NOMAD_VERSION/nomad_${NOMAD_VERSION}_linux_amd64.zip"

RUN apt-get update  -qq && \
    apt-get upgrade -qq && \
    apt-get install -qq -y \
      unzip && \
    apt-clean

RUN curl --location \
         --silent \
         --output /tmp/nomad.zip \
         ${NOMAD_RELEASE} && \
    cd /usr/local/bin && \
    unzip /tmp/nomad.zip && \
    chmod 755 /usr/local/bin/nomad && \
    ln -s /usr/local/bin/nomad /usr/bin/nomad && \
    rm -f /tmp/nomad.zip

CMD [ "nomad", "--version" ]

HEALTHCHECK NONE
# EOF
