FROM alpine:3.3

RUN mkdir /app
WORKDIR /app

ENV PACKAGES "unzip curl openssl ca-certificates git ruby ruby-json"

RUN apk add --update $PACKAGES && rm -rf /var/cache/apk/*

# Make a directory for CloudFoundry storage
RUN mkdir /cf
ENV CF_PLUGIN_HOME /cf

RUN curl -L 'https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.26.0' | tar -zx -C /usr/local/bin
RUN curl -L 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64' -o /usr/local/bin/jq && chmod +x /usr/local/bin/jq

RUN cf install-plugin targets -f -r CF-Community
RUN cf install-plugin autopilot -f -r CF-Community
RUN cf install-plugin https://github.com/18F/cg-migrate-db/releases/download/v0.0.3/linux-64-cg-migrate-db -f
