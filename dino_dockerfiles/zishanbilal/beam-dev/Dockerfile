FROM anapsix/alpine-java:8_jdk

MAINTAINER zishanbilal <zeeshan.bilal@northstar-its.com>

CMD ["gradle"]

ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.0

ARG GRADLE_DOWNLOAD_SHA256=56bd2dde29ba2a93903c557da1745cafd72cdd8b6b0b83c05a40ed7896b79dfe
RUN set -o errexit -o nounset \
	&& echo "Installing dependencies" \
	&& apk add --no-cache \
		bash \
		libstdc++ \
	\
	&& echo "Installing build dependencies" \
	&& apk add --no-cache --virtual .build-deps \
		ca-certificates \
		openssl \
		unzip \
	\
	&& echo "Downloading Gradle" \
	&& wget -O gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
	\
	&& echo "Checking download hash" \
	&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum -c - \
	\
	&& echo "Installing Gradle" \
	&& unzip gradle.zip \
	&& rm gradle.zip \
	&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
	&& ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \
	\
	&& apk del .build-deps \
	\
	&& echo "Adding dev user and group" \
	&& addgroup -S -g 1000 dev \
	&& adduser -D -S -G dev -u 1000 -s /bin/ash dev \
	&& mkdir /home/dev/.gradle \
	&& chown -R dev:dev /home/dev

# Create Gradle volume
USER dev
VOLUME "/home/dev/.gradle"
VOLUME "/home/dev"

WORKDIR /home/dev

RUN set -o errexit -o nounset \
	&& echo "Testing Gradle installation" \
	&& gradle --version
