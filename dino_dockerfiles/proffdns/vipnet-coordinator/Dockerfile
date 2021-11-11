FROM ubuntu:latest
MAINTAINER Denis Malyshev <proffdns@mail.ru>
ENV DEBIAN_FRONTEND noninteractive
#
RUN apt-get update && apt-get install -y --no-install-recommends linux-headers-$(uname -r) net-tools ethtool psmisc patch make kmod gcc
#
ENTRYPOINT ["/bin/bash"]
