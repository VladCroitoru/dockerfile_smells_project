# Builds a Docker image for Overture from github in a Desktop environment
# with Ubuntu and LXDE in serial with PETSc 3.8.x.
#
# The built image can be found at:
#   https://hub.docker.com/r/unifem/overture-desktop
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# The installation procedure follows the (somewhat-oudated) Guide at
# See http://www.overtureframework.org/documentation/install.pdf

# Use meshdb-desktop as base image
FROM unifem/overture-desktop:framework
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER $DOCKER_USER

# Compile CG in serial
ENV CG=$DOCKER_HOME/overture/cg
ENV CGBUILDPREFIX=$DOCKER_HOME/overture/cg.bin

RUN cd $CG && git pull https next && \
    make -j2 usePETSc=on OV_USE_PETSC_3=1 libCommon && \
    make -j2 usePETSc=on OV_USE_PETSC_3=1 cgad cgcns cgins cgasf cgsm cgmp && \
    mkdir -p $CGBUILDPREFIX/bin && \
    ln -s -f $CGBUILDPREFIX/*/bin/* $CGBUILDPREFIX/bin && \
    \
    echo "export PATH=$CGBUILDPREFIX/bin:\$PATH:." >> \
        $DOCKER_HOME/.profile

USER root
WORKDIR /tmp

WORKDIR $DOCKER_HOME
