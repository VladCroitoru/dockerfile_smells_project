# Builds a Docker image with Ubuntu, Octave, Python3 and
# Jupyter Notebook for FastSolve
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM fastsolve/desktop:base
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install ilupack4m, paracoder and petsc4m
RUN git clone --depth 1 https://github.com/hpdata/gdutil /usr/local/gdutil && \
    pip3 install -r /usr/local/gdutil/requirements.txt && \
    ln -s -f /usr/local/gdutil/bin/* /usr/local/bin/ && \
    \
    mkdir -p /usr/local/paracoder && \
    curl -s  -L https://github.com/fastsolve/paracoder/archive/master.tar.gz | \
        bsdtar zxf - --strip-components 1 -C /usr/local/paracoder && \
    cd /usr/local/paracoder && octave --eval "build_m2c -force" && \
    rm -rf `find /usr/local/paracoder -name lib` && \
    \
    mkdir -p /usr/local/ilupack4m && \
    curl -s  -L https://github.com/fastsolve/ilupack4m/archive/master.tar.gz | \
        bsdtar zxf - --strip-components 1 -C /usr/local/ilupack4m && \
    cd /usr/local/ilupack4m && octave --eval "build_milu" && \
    \
    mkdir -p /usr/local/petsc4m && \
    curl -s  -L https://github.com/fastsolve/petsc4m/archive/master.tar.gz | \
        bsdtar zxf - --strip-components 1 -C /usr/local/petsc4m && \
    cd /usr/local/petsc4m && octave --eval "build_petsc -force" && \
    rm -rf `find /usr/local/petsc4m -name lib` && \
    \
    echo 'run /usr/local/paracoder/startup.m' >> $DOCKER_HOME/.octaverc && \
    echo 'run /usr/local/ilupack4m/startup.m' >> $DOCKER_HOME/.octaverc && \
    echo 'run /usr/local/petsc4m/startup.m' >> $DOCKER_HOME/.octaverc && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME

WORKDIR $DOCKER_HOME
