FROM ubuntu:trusty
MAINTAINER ASCDC <ascdc@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install nfs-common nfs-client
ADD mount.sh /mount.sh
RUN chmod +x /*.sh

ENV IP **None**
ENV OPT **None**
ENV SOURCE **None**
ENV TARGET **None**

ENTRYPOINT ["/mount.sh"]
