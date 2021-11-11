#
# Node 0.12 Runner Image
# Docker image with tools and scripts installed to support the running of a Node 0.12 web app
# Primarily designed for the hosting of static content, but also supports config loading via ngConstant for Angular 1
# Expects build artifacts mounted at /home/runner/artifacts
#

FROM mhart/alpine-node:0.12
MAINTAINER Agile Digital <info@agiledigital.com.au>
LABEL Description=" Docker image with tools and scripts installed to support the running of a Node 0.12 web app" Vendor="Agile Digital" Version="0.1"

ENV HOME /home/runner
WORKDIR /home/runner

RUN apk add --update --no-cache git bash openjdk8-jre curl
RUN addgroup -S -g 10000 runner
RUN adduser -S -u 10000 -h $HOME -G runner runner

RUN apk add --update bash openjdk7-jre curl

# Install envplate for stamping out the conf files at run time.
RUN curl -sLo /usr/local/bin/ep https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux && chmod +x /usr/local/bin/ep

# AWS cli
RUN apk add python py-pip \
    && pip --no-cache-dir install --upgrade pip setuptools \
    && pip --no-cache-dir install awscli

COPY app /home/runner/app
COPY tools /home/runner/tools

WORKDIR /home/runner/app

RUN chown -R runner /home/runner/app

RUN npm install

RUN npm install -g grunt-cli

# Must match the port in server.js
EXPOSE 8000

RUN chmod +x /home/runner/app/prepare.sh
RUN chmod +x /home/runner/app/run.sh
RUN chmod +x /home/runner/tools/generate_config_json.sh

# We need to support Openshift's random userid's
# Openshift leaves the group as root. Exploit this to ensure we can always write to them
# Ensure we are in the the passwd file
RUN chmod g+w /etc/passwd
RUN chgrp -Rf root /home/runner && chmod -Rf g+w /home/runner
ENV RUNNER_USER runner

USER runner

ENTRYPOINT [ "/home/runner/app/run.sh" ]
