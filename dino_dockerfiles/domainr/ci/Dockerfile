# domainr/ci Dockerfile
#
# We work in two steps: as root, then as not-root.
# We use two stages, so that we can --target=rootstage to do other work.
#
# Multi-stage Dockerfile requires Docker 17.05 or higher.

# Note:
# ARG goes out of scope on the next FROM line, so any ARGs wanted have to be
# repeated in the context where you want them.  However, there's special
# treatment for any ARG which is declared before the very first FROM: the
# values become the defaults for later ARG of the same name, and these ARGs
# (and _only_ these ones) are available for use in the FROM lines themselves.
#
# Also, note that LABELs persist across inheritance boundaries, unless
# overridden.

ARG GOLANG_VERSION=1.15.3
ARG RUNTIME_USER=domainr
ARG RUNTIME_UID=1001
ARG RUNTIME_GID=1001

# Base image:
# https://hub.docker.com/r/circleci/golang
ARG GOLANG_BASE_IMAGE=circleci/golang:${GOLANG_VERSION}-buster-node-browsers

# Neat/Evil hack: while in CI, we use Docker-in-Docker, for local development
# it's nicer to bind-mount /var/run/docker.sock into the instance, so that
# you can run `docker ps` and see the outside docker.  The permissions and
# numeric ownership remain unchanged between the outside and inside.
# Using `docker-machine` (Boot2Docker version 18.02.0-ce), the socket is
# 0660 root:docker, where group docker is 100.  Assuming that we're derived
# from stretch (per default) group 100 is "users", which is _entirely_
# reasonable for the only runtime user to be a member of.  So go for it.
# Keep this as a comma-separated list of non-negative integers.
ARG RUNTIME_SUPGIDS=100

# -------------------------8< Stage: rootstage >8-------------------------

FROM ${GOLANG_BASE_IMAGE} AS rootstage

# Need root user for apt-get
USER root

ARG GOLANG_BASE_IMAGE
#
# Only for stamping into the labels, and tracking
ARG GOLANG_VERSION
#
# Dep readme says "It is strongly recommended that you use a released version."
ARG DEP_VERSION
#
ARG RUNTIME_USER
ARG RUNTIME_UID
ARG RUNTIME_GID
ARG RUNTIME_SUPGIDS
# Persisting this in ENV makes it available to RUN commands in the second stage:
ENV RUNTIME_USER=${RUNTIME_USER}

# need 'zip' for slug build
# need 'nc' for sanity checks in one project; deb netcat-traditional
# need 'git-hub' for GitHub's hub command, for one-off runners using this CI image
#   but link it to the more common name found outside Debian, too
# need 'less' for sanity

RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true; \
	apt-get update \
	&& apt-get -q -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confnew" upgrade \
	&& apt-get install -q -y --no-install-recommends \
		apt-transport-https \
		software-properties-common \
		netcat-traditional netcat zip \
		git-hub less \
	&& ln -s /usr/bin/git-hub /usr/local/bin/hub
# defer removing /var/lib/apt/lists/* until done with apt-get below

# For the trust reduction, see:
#  <https://wiki.debian.org/DebianRepository/UseThirdParty>
#  <https://public-packages.pennock.tech/>
#
RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true; \
	echo "Adding docker repositories and installing Docker" \
	&& mkdir -pv /etc/apt/keys /etc/apt/preferences.d \
	&& curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | gpg --dearmor > /etc/apt/keys/docker.gpg \
	&& printf > /etc/apt/preferences.d/docker.pref 'Package: *\nPin: origin download.docker.com\nPin-Priority: 100\n' \
	&& echo \
		"deb [arch=amd64 signed-by=/etc/apt/keys/docker.gpg] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")" \
		$(lsb_release -cs) \
		stable \
		> /etc/apt/sources.list.d/docker.list \
	&& apt-get update \
	&& apt-get -q -y install docker-ce \
	&& rm -rf /var/lib/apt/lists/*

RUN groupadd -g "${RUNTIME_GID}" "${RUNTIME_USER}" && \
    useradd -p '*' -u "${RUNTIME_UID}" -g "${RUNTIME_USER}" -G "${RUNTIME_SUPGIDS}" -m "${RUNTIME_USER}"

# Install Heroku
RUN cd /tmp \
	&& curl -fsSL "https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-linux-x64.tar.gz" -o heroku.tar.gz \
	&& tar -zxf heroku.tar.gz \
	&& mv heroku-cli-*-linux-x64 /usr/local/lib/heroku \
	&& ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku \
	&& rm heroku.tar.gz \
	&& heroku version

# Copy in local scripts
COPY cmd/* /usr/local/bin/
RUN chmod -v +x /usr/local/bin/*

WORKDIR /
# We don't use /go because we don't build as root and 777 permissions are daft
RUN rm -rf /go

LABEL maintainer="ops+docker+ci@domainr.com"
LABEL com.domainr.name="Domainr Continuous Integration (root-stage)"
LABEL com.domainr.baseimage="${GOLANG_BASE_IMAGE}"
LABEL com.domainr.versions.go="${GOLANG_VERSION}"
LABEL com.domainr.runtime.username="root"
LABEL com.domainr.runtime.uid="0"
LABEL com.domainr.runtime.gid="0"
LABEL com.domainr.runtime.unprivileged="${RUNTIME_USER}"

# ----------------------8< Stage: generated image >8----------------------

FROM rootstage

# I've checked, and the ENV persisence of an ARG in the first stage makes the
# value available for WORKDIR/USER directives, etc.

WORKDIR /home/${RUNTIME_USER}
# nb: we don't have a password and have not set up sudo, so no way back at this
# point.  Do we _want_ to still have root?
USER ${RUNTIME_USER}
# Want to just remove the Go image's GOPATH setting but while we can replace
# ENV in Docker, we can't unset.  So suck it up and just set it, old style.
ENV GOPATH=/home/${RUNTIME_USER}/go
ENV PATH=${GOPATH}/bin:/usr/local/go/bin:$PATH

# Install our Go tools
RUN go version && \
	go get -u -v github.com/jstemmer/go-junit-report && \
	go get -u -v github.com/nbio/slugger && \
	go get -u -v github.com/nbio/cart && \
	true

# Labels
ARG RUNTIME_UID
ARG RUNTIME_GID
ARG RUNTIME_SUPGIDS
LABEL com.domainr.name="Domainr Continuous Integration"
LABEL com.domainr.runtime.username="${RUNTIME_USER}"
LABEL com.domainr.runtime.uid="${RUNTIME_UID}"
LABEL com.domainr.runtime.gid="${RUNTIME_GID}"
LABEL com.domainr.runtime.supgids="${RUNTIME_SUPGIDS}"
