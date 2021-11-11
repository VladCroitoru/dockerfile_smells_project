# Dockerfile to create Rosa linux base images
# Create base image with mkimage-urpmi.sh script
#

FROM scratch
MAINTAINER "Anton Goroshkin" <neobht@sibsau.ru>
#ENV TARROOTFS https://github.com/sibsau/docker-rosa/raw/master/rootfs.tar.xz /
ENV TARROOTFS rootfs.tar.xz
ADD ${TARROOTFS} /

CMD ["/bin/bash"]
