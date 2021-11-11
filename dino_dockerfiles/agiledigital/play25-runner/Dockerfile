#
# Play 2.5 Runner Image
# Docker image with tools and scripts installed to support the running of a Play Framework 2.5 server
# Expects build artifacts mounted at /home/runner/artifacts
#

FROM frolvlad/alpine-oraclejdk8
MAINTAINER Agile Digital <info@agiledigital.com.au>
LABEL Description=" Docker image with tools and scripts installed to support the running of a Play Framework 2.5 server" Vendor="Agile Digital" Version="0.1"

ENV HOME /home/runner
WORKDIR /home/runner

# Install libsodium so that applications can use the kalium crypto library.
RUN apk add --update --no-cache git bash tzdata libsodium
RUN addgroup -S -g 10000 runner
RUN adduser -S -u 10000 -h $HOME -G runner runner

# AWS cli
RUN apk add python py-pip \
    && pip --no-cache-dir install --upgrade pip setuptools \
    && pip --no-cache-dir install awscli

COPY tools /home/runner/tools
RUN chmod +x /home/runner/tools/prepare.sh
RUN chmod +x /home/runner/tools/run.sh

# We need to support Openshift's random userid's
# Openshift leaves the group as root. Exploit this to ensure we can always write to them
# Ensure we are in the the passwd file
RUN chmod g+w /etc/passwd
RUN chgrp -Rf root /home/runner && chmod -Rf g+w /home/runner
ENV RUNNER_USER runner

EXPOSE 9000

USER runner

ENTRYPOINT ["/home/runner/tools/run.sh"]
