###   Start by creating a "builder"   ###
# We'll compile all needed packages in the builder, and then
# we'll just get only what we need for the actual APP

ARG DEBIAN_VERSION=buster
ARG BASE_PYTHON_VERSION=3.8
# (don't use simply PYTHON_VERSION because it's an env variable)

# Use an official Python runtime as a parent image
FROM python:${BASE_PYTHON_VERSION}-slim-${DEBIAN_VERSION} as builder

## install the gcc compiler
#  (needed to install some of the python packages):
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    g++ \
    pkg-config \
    make \
    cmake \
    # also install 'curl':
    curl \
  && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y

# Install dcmstack from github:
ENV DCMSTACK_VERSION=v0.8
RUN mkdir /tmp/dcmstack && \
    curl -sSL https://github.com/moloney/dcmstack/archive/${DCMSTACK_VERSION}.tar.gz \
        | tar -vxz -C /tmp/dcmstack --strip-components=1 && \
    cd /tmp/dcmstack && \
    python setup.py install && \
    cd / && rm -rf /tmp/dcmstack

# Install dcm2niix from github (it requires git to "superbuild"):
# Install also pigz-- it makes dcm2niix compress NIfTI files faster
ENV DCM2NIIX_VERSION=v1.0.20210317
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y pigz git-core && \
    apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \
    \
    mkdir /tmp/dcm2niix && \
    curl -sSL https://github.com/rordenlab/dcm2niix/archive/${DCM2NIIX_VERSION}.tar.gz \
        | tar -vxz -C /tmp/dcm2niix --strip-components=1 && \
    cd /tmp/dcm2niix && \
    mkdir build && cd build && cmake -DBATCH_VERSION=ON .. && \
    make && make install && \
    cd / && rm -rf /tmp/dcm2niix

# Install bidsphysio from github:
RUN mkdir /tmp/bidsphysio && \
    curl -sSL https://github.com/cbinyu/bidsphysio/archive/master.tar.gz \
        | tar -vxz -C /tmp/bidsphysio --strip-components=1 && \
    cd /tmp/bidsphysio && \
    pip install . && \
    cd / && \
    rm -rf /tmp/bidsphysio

# Install heudiconv from github:
ENV CBIHEUDICONV_VERSION=v3.7.0
RUN mkdir /tmp/heudiconv && \
    curl -sSL https://github.com/cbinyu/heudiconv/archive/${CBIHEUDICONV_VERSION}.tar.gz \
        | tar -vxz -C /tmp/heudiconv --strip-components=1 && \
    cd /tmp/heudiconv && \
    pip install . && \
    cd / && rm -rf /tmp/heudiconv
#COPY [".", "/tmp/heudiconv"]
#RUN cd /tmp/heudiconv && \
#    pip install . && \
#    cd / && rm -rf /tmp/heudiconv


# Get rid of some test folders in some of the Python packages:
# (They are not needed for our APP):
ENV PYTHON_LIB_PATH=/usr/local/lib/python${BASE_PYTHON_VERSION}
#RUN rm -fr ${PYTHON_LIB_PATH}/site-packages/numpy
RUN rm -fr ${PYTHON_LIB_PATH}/site-packages/nibabel/nicom/tests && \
    rm -fr ${PYTHON_LIB_PATH}/site-packages/nibabel/tests       && \
    rm -fr ${PYTHON_LIB_PATH}/site-packages/nibabel/gifti/tests

#############

###  Now, get a new machine with only the essentials  ###

FROM python:${BASE_PYTHON_VERSION}-slim-${DEBIAN_VERSION} as Application

# This makes the BASE_PYTHON_VERSION available inside this stage
ARG BASE_PYTHON_VERSION
ENV PYTHON_LIB_PATH=/usr/local/lib/python${BASE_PYTHON_VERSION}

COPY --from=builder ./${PYTHON_LIB_PATH}/       ${PYTHON_LIB_PATH}/
COPY --from=builder ./usr/local/bin/           /usr/local/bin/
COPY --from=builder ./usr/bin/pigz             /usr/bin/

ENTRYPOINT ["/usr/local/bin/heudiconv"]
