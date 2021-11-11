# This container is intended to use htpasswd basic auth and simplify adding credentials for a docker registry

FROM registry:2
MAINTAINER ben@tozny.com

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
