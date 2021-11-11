#
# Ubuntu 14.04 with quassel-core Dockerfile
#
# Pull base image.
FROM eternnoir/ubuntu-14.04-sshd
MAINTAINER Frank Wang "eternnoir@gmail.com"

#Update
RUN apt-get update && apt-get install -y quassel-core
VOLUME ["/var/lib/quassel"]
EXPOSE 4242
CMD ["quasselcore", "--configdir=/var/lib/quassel/"]
