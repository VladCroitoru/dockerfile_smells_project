# Builds a Docker image for Multithreaded version of CalculiX
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM x11vnc/desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp
ADD image/usr /usr

# Install system packages
RUN sh -c "curl -s http://dl.openfoam.org/gpg.key | apt-key add -" && \
    add-apt-repository http://dl.openfoam.org/ubuntu && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        gfortran \
        git \
        paraviewopenfoam56 && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Checkout CalcluiX_MT and compile it with Spooles and OpenMP
RUN git clone https://github.com/unifem/CalculiX_MT.git calculix && \
    cd calculix && \
    perl -e 's/https:\/\/[\w:\.]+@([\w\.]+)\//git\@$1:/' -p -i .git/config && \
    git remote add https https://github.com/unifem/CalculiX_MT.git && \
    CALCULIX_HOME=$PWD ./build_ccx


########################################################
# Customization for user
########################################################
RUN echo "export OMP_NUM_THREADS=\$(nproc)" >> $DOCKER_HOME/.profile && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME

WORKDIR $DOCKER_HOME
