FROM buildkite/agent:3

# We use top-level mount dirs so it works with nfs properly
VOLUME /buildkite-builds
VOLUME /buildkite-secrets

RUN apk add --no-cache \
	e2fsprogs \
	iptables

# Add the hyper binary
# Adds sgerrand’s glibc compat layer for the hyper binary
# https://github.com/sgerrand/alpine-pkg-glibc
ARG GLIBC_VERSION=2.25-r0
RUN apk --no-cache add ca-certificates \
    && curl -Lfs https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub > /etc/apk/keys/sgerrand.rsa.pub \
    && curl -Lfs https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk > /tmp/glibc.apk \
    && apk add /tmp/glibc.apk \
    && rm /tmp/glibc.apk /etc/apk/keys/sgerrand.rsa.pub \
    && curl -Ls https://hyper-install.s3.amazonaws.com/hyper-linux-x86_64.tar.gz | tar xz \
    && mv hyper /usr/bin/hyper \
    && chmod +x /usr/bin/hyper

COPY entrypoint.sh /entrypoint.sh
COPY buildkite-agent-bootstrap.sh /buildkite/hyper-bootstrap
COPY buildkite-agent-post-command.sh /buildkite/hooks/post-command

ENV HYPER_SCHEDULER="false"
ENV HYPER_RUNNER_SIZE="S4"

ENV BUILDKITE_AGENT_NAME="hyper-agent-%n"
ENV BUILDKITE_BUILD_PATH="/buildkite-builds"
ENV BUILDKITE_BOOTSTRAP_SCRIPT_PATH=/buildkite/hyper-bootstrap
ENV BUILDKITE_HOOKS_PATH=/buildkite/hooks
ENV BUILDKITE_AGENT_EXIT_AFTER_JOB="false"

ENV TINI_SUBREAPER=true

ENTRYPOINT ["/sbin/tini", "-g", "--", "/entrypoint.sh", "buildkite-agent-entrypoint"]
