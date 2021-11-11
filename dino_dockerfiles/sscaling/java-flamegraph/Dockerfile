FROM 		openjdk:8-alpine
MAINTAINER	sscaling <shaun@shaunscaling.com>

# Install any dependencies
RUN apk add --update \
    perl \
    curl \
  && rm -rf /var/cache/apk/*

# Get JavaFX
# According to https://github.com/jvm-profiling-tools/honest-profiler/wiki/How-to-build use the the javafx overlay
# from https://www.chrisnewland.com/openjfx
RUN	curl -o /tmp/openjfx.zip http://108.61.191.178/downloads/openjfx-8u60-sdk-overlay-linux-amd64.zip \
	&& unzip -o -d /usr/lib/jvm/java-1.8-openjdk/ /tmp/openjfx.zip \
	&& rm /tmp/openjfx.zip

# Grab honest profiler
RUN	wget http://insightfullogic.com/honest-profiler.zip \
	&& unzip -o -d /usr/local/bin honest-profiler.zip \
	&& rm honest-profiler.zip

# Grab flamegraph
RUN	curl -o /usr/local/bin/flamegraph.pl https://raw.githubusercontent.com/brendangregg/FlameGraph/master/flamegraph.pl \
	&& chmod +x /usr/local/bin/flamegraph.pl

COPY	start.sh /

WORKDIR	/source

ENTRYPOINT ["/start.sh"]

