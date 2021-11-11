FROM debian:stretch-slim

RUN set -exu && \
mkdir -p /etc/dpkg/dpkg.conf.d && \
touch /etc/dpkg/dpkg.conf.d/01_nodoc && \
for e in doc-base doc groff info linda lintian man;\
  do echo "path-exclude /usr/share/${e}/*" >> /etc/dpkg/dpkg.conf.d/01_nodoc;\
done && \
export DEBIAN_FRONTEND=noninteractive && \
apt-get update -qq && \
apt-get install -qqyu --auto-remove --no-install-recommends --no-install-suggests apt-transport-https && \
rm -r /var/lib/apt/lists/* /etc/dpkg/dpkg.conf.d/
