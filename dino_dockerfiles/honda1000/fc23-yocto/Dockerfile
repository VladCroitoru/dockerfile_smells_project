FROM fedora:23
MAINTAINER r31988 <atsushi.honda@nxp.com>

RUN dnf -y update && dnf -y install vim sudo

RUN echo 'root:root' | chpasswd

RUN groupadd -g 1000 r31988 && \
    useradd -g r31988 -G root -m -s /bin/bash r31988 && \
    echo 'r31988:r31988' | chpasswd

USER r31988
