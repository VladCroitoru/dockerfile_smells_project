# Docker container containing jq

FROM alpine:3.6
MAINTAINER Jason Crowe <jcrowe@mozilla.com>

# Install container dependencies
#+ Cleanup apk cache files
RUN apk add --no-cache \
    jq=1.5-r3 \
    && rm -f /var/cache/apk/APKINDEX.*
