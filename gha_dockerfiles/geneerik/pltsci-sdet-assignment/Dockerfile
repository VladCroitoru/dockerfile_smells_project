# The details can be found in the following web page.
# https://codecept.io/docker.html
# Note: codeceptjs have not tagged their "latest" build with a persistent (ala 3.04) version tag =(
ARG IMAGE_VERSION=${IMAGE_VERSION:-latest}
ARG REGISTRY_URI=${REGISTRY_URI:-}
ARG IMAGE_NAME=${IMAGE_NAME:-codeceptjs/codeceptjs}
FROM ${REGISTRY_URI}${IMAGE_NAME}:${IMAGE_VERSION} as base

# fix pwuser groups
RUN usermod -aG audio,video,www-data pwuser

# setup server logging directory and future link to allure binary for reporting
RUN APPLICATION_HOME=/usr/local/demo-app; \
    TEST_DIR=/src/test/javascript/sdet-assignment-service-codeceptsjs; \
    #mkdir -p "${APPLICATION_HOME}"/logs && \
    #chmod 777 "${APPLICATION_HOME}"/logs && \
    ln -sf "${TEST_DIR}"/node_modules/allure-commandline/dist/bin/allure /usr/local/bin/allure

# Enable headless (cli) package installs
ARG DEBIAN_FRONTEND=noninteractive

## Java stuff (needed for reporting)
# curl setup

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		netbase \
		wget \
	; \
	rm -rf /var/lib/apt/lists/*

RUN set -ex; \
	if ! command -v gpg > /dev/null; then \
		apt-get update; \
		apt-get install -y --no-install-recommends \
			gnupg \
			dirmngr \
		; \
		rm -rf /var/lib/apt/lists/*; \
	fi

# scm setup

# procps is very common in build systems, and is a reasonably small package
RUN apt-get update && apt-get install -y --no-install-recommends \
		git \
		mercurial \
		openssh-client \
		subversion \
		\
		procps \
	&& rm -rf /var/lib/apt/lists/*

# java setup

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		bzip2 \
		unzip \
		xz-utils \
		\
# java.lang.UnsatisfiedLinkError: /usr/local/openjdk-11/lib/libfontmanager.so: libfreetype.so.6: cannot open shared object file: No such file or directory
# java.lang.NoClassDefFoundError: Could not initialize class sun.awt.X11FontManager
# https://github.com/docker-library/openjdk/pull/235#issuecomment-424466077
		fontconfig libfreetype6 \
		\
# utilities for keeping Debian and OpenJDK CA certificates in sync
		ca-certificates p11-kit \
	; \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/local/openjdk-8
RUN { echo '#/bin/sh'; echo 'echo "$JAVA_HOME"'; } > /usr/local/bin/docker-java-home && chmod +x /usr/local/bin/docker-java-home && [ "$JAVA_HOME" = "$(docker-java-home)" ] # backwards compatibility
ENV PATH $JAVA_HOME/bin:$PATH

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# https://adoptopenjdk.net/upstream.html
# >
# > What are these binaries?
# >
# > These binaries are built by Red Hat on their infrastructure on behalf of the OpenJDK jdk8u and jdk11u projects. The binaries are created from the unmodified source code at OpenJDK. Although no formal support agreement is provided, please report any bugs you may find to https://bugs.java.com/.
# >
ENV JAVA_VERSION 8u302
# https://github.com/docker-library/openjdk/issues/320#issuecomment-494050246
# >
# > I am the OpenJDK 8 and 11 Updates OpenJDK project lead.
# > ...
# > While it is true that the OpenJDK Governing Board has not sanctioned those releases, they (or rather we, since I am a member) didn't sanction Oracle's OpenJDK releases either. As far as I am aware, the lead of an OpenJDK project is entitled to release binary builds, and there is clearly a need for them.
# >

RUN set -eux; \
	\
	arch="$(dpkg --print-architecture)"; \
	case "$arch" in \
		'amd64') \
			downloadUrl='https://github.com/AdoptOpenJDK/openjdk8-upstream-binaries/releases/download/jdk8u302-b08/OpenJDK8U-jdk_x64_linux_8u302b08.tar.gz'; \
			;; \
		'arm64') \
			downloadUrl='https://github.com/AdoptOpenJDK/openjdk8-upstream-binaries/releases/download/jdk8u302-b08/OpenJDK8U-jdk_aarch64_linux_8u302b08.tar.gz'; \
			;; \
		*) echo >&2 "error: unsupported architecture: '$arch'"; exit 1 ;; \
	esac; \
	\
	wget --progress=dot:giga -O openjdk.tgz "$downloadUrl"; \
	wget --progress=dot:giga -O openjdk.tgz.asc "$downloadUrl.sign"; \
	\
	export GNUPGHOME="$(mktemp -d)"; \
# pre-fetch Andrew Haley's (the OpenJDK 8 and 11 Updates OpenJDK project lead) key so we can verify that the OpenJDK key was signed by it
# (https://github.com/docker-library/openjdk/pull/322#discussion_r286839190)
# we pre-fetch this so that the signature it makes on the OpenJDK key can survive "import-clean" in gpg
	gpg --batch --keyserver keyserver.ubuntu.com --recv-keys EAC843EBD3EFDB98CC772FADA5CD6035332FA671; \
# TODO find a good link for users to verify this key is right (https://mail.openjdk.java.net/pipermail/jdk-updates-dev/2019-April/000951.html is one of the only mentions of it I can find); perhaps a note added to https://adoptopenjdk.net/upstream.html would make sense?
# no-self-sigs-only: https://salsa.debian.org/debian/gnupg2/commit/c93ca04a53569916308b369c8b218dad5ae8fe07
	gpg --batch --keyserver keyserver.ubuntu.com --keyserver-options no-self-sigs-only --recv-keys CA5F11C6CE22644D42C6AC4492EF8D39DC13168F; \
	gpg --batch --list-sigs --keyid-format 0xLONG CA5F11C6CE22644D42C6AC4492EF8D39DC13168F \
		| tee /dev/stderr \
		| grep '0xA5CD6035332FA671' \
		| grep 'Andrew Haley'; \
	gpg --batch --verify openjdk.tgz.asc openjdk.tgz; \
	gpgconf --kill all; \
	rm -rf "$GNUPGHOME"; \
	\
	mkdir -p "$JAVA_HOME"; \
	tar --extract \
		--file openjdk.tgz \
		--directory "$JAVA_HOME" \
		--strip-components 1 \
		--no-same-owner \
	; \
	rm openjdk.tgz*; \
	\
# update "cacerts" bundle to use Debian's CA certificates (and make sure it stays up-to-date with changes to Debian's store)
# see https://github.com/docker-library/openjdk/issues/327
#     http://rabexc.org/posts/certificates-not-working-java#comment-4099504075
#     https://salsa.debian.org/java-team/ca-certificates-java/blob/3e51a84e9104823319abeb31f880580e46f45a98/debian/jks-keystore.hook.in
#     https://git.alpinelinux.org/aports/tree/community/java-cacerts/APKBUILD?id=761af65f38b4570093461e6546dcf6b179d2b624#n29
	{ \
		echo '#!/usr/bin/env bash'; \
		echo 'set -Eeuo pipefail'; \
		echo 'trust extract --overwrite --format=java-cacerts --filter=ca-anchors --purpose=server-auth "$JAVA_HOME/jre/lib/security/cacerts"'; \
	} > /etc/ca-certificates/update.d/docker-openjdk; \
	chmod +x /etc/ca-certificates/update.d/docker-openjdk; \
	/etc/ca-certificates/update.d/docker-openjdk; \
	\
# https://github.com/docker-library/openjdk/issues/331#issuecomment-498834472
	find "$JAVA_HOME/lib" -name '*.so' -exec dirname '{}' ';' | sort -u > /etc/ld.so.conf.d/docker-openjdk.conf; \
	ldconfig; \
	\
# basic smoke test
	javac -version; \
	java -version
## end java stuff

# prepare for node_modules. update npm
RUN mkdir -p /npm_packages && \
    mkdir -p /src/test/javascript/sdet-assignment-service-codeceptsjs && \
    npm install -g npm && \
    which -a npm && \
    npm --version

# Copy in the package requirements and resolve them
COPY /src/test/javascript/sdet-assignment-service-codeceptsjs/package*.json /src/test/javascript/sdet-assignment-service-codeceptsjs/
# make sure non-root can install node_modules.
RUN chown pwuser:pwuser -R /src/test/javascript/sdet-assignment-service-codeceptsjs

USER pwuser
RUN cd /src/test/javascript/sdet-assignment-service-codeceptsjs && \
    ls -la && \
    which -a npm && \
    npm --version && \
    npm install --include=dev && \
    npx playwright install && \
    which -a npm && \
    npm --version
USER 0
# Move the node_modules to a backup location and nuke /src for copy
RUN cd /npm_packages && \
    mv /src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules . && \
    mv /src/test/javascript/sdet-assignment-service-codeceptsjs/package-lock.json . && \
    rm -rf /src

# enable upgrade periodic (daily) trigger and do upgrades
ARG UPDATE_TIMESTAMP
RUN (date > /etc/geneerik_apt_date) && \
    apt-get update -y && \
    apt-get -o Dpkg::Options::="--force-confold" upgrade -y && \
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Copy in the tests
COPY /src /src

# Fix the package lock file and link in the node_modules directory
RUN cd /src/test/javascript/sdet-assignment-service-codeceptsjs && \
    cp -a /npm_packages/package-lock.json . && \
    cp -a /npm_packages/node_modules . && \
    # Fix npm.  again.
    npm install -g npm && \
    which -a npm && \
    npm --version

COPY application-logging.properties /src/test/javascript/sdet-assignment-service-codeceptsjs/

# entrypoint script to setup server logging stuff
COPY test_compose_init_entrypoint.sh /

WORKDIR /src/test/javascript/sdet-assignment-service-codeceptsjs

USER pwuser

# install packages (if needed; unlikely, but quick step.  can show new vulns/package issues)
RUN which -a npm && \
    npm --version && \
    npm install --include=dev && \
    npx playwright install && \
    #npx codeceptjs def
    echo "build success"

# codeceptjs needs a special patch to allow a successful exit code when tests fail; applying the patch here
### in the eixt listener
#    if (failedTests.length) {
###
### needs to be changed to
#    if ((process.env.ALLOW_TEST_FAILURES ?? "false").toLocaleLowerCase() !== "true"  && failedTests.length) {
### and in the workers vlass isFailed method
#    return (this.stats.failures || this.errors.length) > 0;
### needs to be changed to
#    return ((process.env.ALLOW_TEST_FAILURES ?? "false").toLocaleLowerCase() !== "true"  && this.stats.failures > 0) || this.errors.length > 0;
# This patch allows this to be enabled on environmental variable ALLOW_TEST_FAILURES having a value of "true". There is presently no way to do this using normal config or parameters

RUN sed -i "s/^\\( *\\)if (failedTests.length) {\$/\\1if ((process.env.ALLOW_TEST_FAILURES ?? \"false\").toLowerCase() !== \"true\" \\&\\& failedTests.length) {/" '/src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules/codeceptjs/lib/listener/exit.js' && \
	sed -i "s/\\( *\\)return (this.stats.failures || this.errors.length) > 0;\$/\\1return ((process.env.ALLOW_TEST_FAILURES ?? \"false\").toLowerCase() !== \"true\" \\&\\& this.stats.failures > 0) || this.errors.length > 0;/" '/src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules/codeceptjs/lib/workers.js'

# codeceptjs-ui needs a special patch to be served within docker; applying the patch here
###
#  io.listen(webSocketsPort);
#  app.listen(applicationPort);
###
### needs to be changed to
#  const iohttp = require('http').createServer().listen(webSocketsPort, '0.0.0.0');
#  io.listen(iohttp);
#  app.listen(applicationPort, '0.0.0.0');
# There is presently no way to do this using normal config or parameters

RUN sed -i "s/^\\( *io.listen(\\)\\(webSocketsPort\\)\\();\\.*\\)\$/  const iohttp = require('http').createServer().listen(\\2, '0.0.0.0');\\n\\1iohttp\\3/" '/src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules/@codeceptjs/ui/bin/codecept-ui.js' && \
	sed -i "s/^\\( *app.listen(applicationPort\\)\\();\\.*\\)\$/\\1, '0.0.0.0'\\2/" '/src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules/@codeceptjs/ui/bin/codecept-ui.js'

# Update the entrypoint. Note: CODECEPT_ARGS is no longer used
ENTRYPOINT [ "/usr/bin/node", "/src/test/javascript/sdet-assignment-service-codeceptsjs/node_modules/codeceptjs/bin/codecept.js" ]
CMD [ "run" ]

# Versioning and docker metadata stuff
LABEL org.opencontainers.image.authors='GeneErik <support@fossdevops.com>'
LABEL org.opencontainers.image.url='https://github.com/geneerik/pltsci-sdet-assignment'
LABEL org.opencontainers.image.documentation='https://geneerik.github.io/pltsci-sdet-assignment'
LABEL org.opencontainers.image.source='https://github.com/geneerik/pltsci-sdet-assignment.git'
LABEL org.opencontainers.image.vendor='GeneErik'
#LABEL org.opencontainers.image.licenses=''
LABEL org.opencontainers.image.title='ghcr.io/geneerik/pltsci-sdet-assignment'
LABEL org.opencontainers.image.description="Docker image containing prerequisites and code to execute BDD tests against the com.yoti.sdet.assignment.service web service"

# set version stuff
ARG VERSION=unset
ARG LONG_FORM_VERSION=unset
USER 0
RUN (printf 'com.yoti.sdet.assignment.service.AppRunner e2e Test Container' > /etc/geneerik_product) && \
    (printf '%s' "${VERSION}" > /etc/geneerik_version) && \
    (printf '%s' "${LONG_FORM_VERSION}" > /etc/geneerik_version_long)
USER pwuser