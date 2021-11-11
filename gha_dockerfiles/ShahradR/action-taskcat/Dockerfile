# For v0.9 and higher, the taskcat containers do not pin specific
# versions. Rather, they always fetch the latest version from pip. See
# https://dockr.ly/2BjpG7C to see the taskcat Dockerfile.

# hadolint disable=DL3007
FROM taskcat/taskcat:latest

RUN apk add --no-cache nodejs~=12 npm~=12 && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY dist/index.js /dist/index.js

ENTRYPOINT ["/entrypoint.sh"]
