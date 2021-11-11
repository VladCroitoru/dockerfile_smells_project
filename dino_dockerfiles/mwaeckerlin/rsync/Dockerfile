FROM mwaeckerlin/very-base
MAINTAINER mwaeckerlin

# change in childern:
ENV CONTAINERNAME     "rsync"

RUN apk add --no-cache --purge --clean-protected -u rsync

ENTRYPOINT ["/usr/bin/rsync", "-avP", "--delete"]
