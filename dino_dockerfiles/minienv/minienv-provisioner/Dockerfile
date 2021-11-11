FROM docker:dind

MAINTAINER Mark Watson <markwatsonatx@gmail.com>

RUN apk add --no-cache bash

COPY minienv-provisioner-entrypoint.sh /

ENTRYPOINT ["/minienv-provisioner-entrypoint.sh"]
