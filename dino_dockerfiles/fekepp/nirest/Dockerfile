# Depend on the official Ubuntu 16.04 LTS image
FROM	ubuntu:16.04


# Define maintainer
MAINTAINER "Felix Leif Keppmann <felix.leif@keppmann.de>"


# Add Gradle build file which will be used to determine the version
ADD	build.gradle /root/


# Determine version from Gradle build file and fall back to master in case of snapshots
# Install required dependencies
# Download and compile sources
# Install distribution files
# Remove obsolete files
# Log version and URL
RUN	cd /root/ \
	&& export VERSION=$(cat build.gradle | grep -e "^\s*version = " | sed -e "s/^\s*version = '//"  -e "s/'$//") \
	&& case $VERSION in *"-SNAPSHOT") export VERSION="master";; esac \
	&& export URL="https://github.com/fekepp/nirest/archive/$VERSION.tar.gz" \
	\
	&& apt-get update \
	&& apt-get install -y \
		curl \
		libusb-1.0-0-dev \
		openjdk-8-jdk \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& cd /usr/src/ \
	&& mkdir nirest \
	&& curl -SL "$URL" -o nirest.tar.gz \
	&& tar --strip-components=1 -xzf nirest.tar.gz -C nirest \
	&& cd nirest \
	&& ./gradlew installDist \
	\
	&& mv build/install/nirest /usr/share/ \
	\
	&& cd / \
	&& rm -rf /root/.gradle \
	&& rm -rf /usr/src/nirest \
	&& rm -f /usr/src/nirest.tar.gz \
	\
	&& echo "VERSION=$VERSION" \
	&& echo "URL=$URL"


# Set default entry point
ENTRYPOINT ["/usr/share/nirest/bin/nirest-server"]
