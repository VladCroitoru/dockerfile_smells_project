# Builds a Docker image with OpenFOAM, Calculix and Overture, based on
# Ubuntu 17.10 for multiphysics coupling
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use coupler-desktop:framework as base image
FROM unifem/coupler-desktop:framework
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER $DOCKER_USER

# Compile CG in serial
ENV CG=$DOCKER_HOME/overture/cg
ENV CGBUILDPREFIX=$DOCKER_HOME/overture/cg.bin

RUN cd $CG && git pull https master && \
    make -j2 usePETSc=on OV_USE_PETSC_3=1 libCommon && \
    make -j2 usePETSc=on OV_USE_PETSC_3=1 cgad cgcns cgins cgasf cgsm cgmp && \
    mkdir -p $CGBUILDPREFIX/bin && \
    ln -s -f $CGBUILDPREFIX/*/bin/* $CGBUILDPREFIX/bin && \
    \
    echo "export PATH=$CGBUILDPREFIX/bin:\$PATH:." >> \
        $DOCKER_HOME/.profile

USER root
ADD image/home $DOCKER_HOME
WORKDIR $DOCKER_HOME
