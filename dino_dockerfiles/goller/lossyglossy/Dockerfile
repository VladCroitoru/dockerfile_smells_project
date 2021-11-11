FROM golang:onbuild
MAINTAINER Chris Goller <chris@influxdb.com>
RUN apt-get update && apt-get install -y --no-install-recommends \
		curl \
&& rm -rf /var/lib/apt/lists/*

EXPOSE 8080
HEALTHCHECK --interval=15s --timeout=3s --retries=2 CMD curl -s -k -f https://localhost:8080/health/ || exit 1