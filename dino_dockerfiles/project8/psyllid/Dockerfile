## Note that these IMG_* ARG values are defaults, but actual automated builds use
## values which stored in the .travis.yaml file
ARG IMG_USER=project8
ARG IMG_REPO=p8compute_dependencies
ARG IMG_TAG=v0.9.0

FROM ${IMG_USER}/${IMG_REPO}:${IMG_TAG} as psyllid_common

ARG PSYLLID_PREFIX_TAG=beta
ENV PSYLLID_PREFIX_TAG=${PSYLLID_PREFIX_TAG}
ARG PSYLLID_BASE_PREFIX=/usr/local/p8/psyllid
ARG PSYLLID_BUILD_PREFIX=${PSYLLID_BASE_PREFIX}/${PSYLLID_PREFIX_TAG}
ENV PSYLLID_BUILD_PREFIX=${PSYLLID_BUILD_PREFIX}

SHELL ["/bin/bash", "-c"]

RUN mkdir -p $PSYLLID_BUILD_PREFIX
WORKDIR $PSYLLID_BUILD_PREFIX

RUN echo "export PSYLLID_BUILD_PREFIX=${PSYLLID_BUILD_PREFIX}" >> setup.sh \
    && echo "export PATH=$PSYLLID_BUILD_PREFIX/bin:$PATH" >> setup.sh \
    && echo "export LD_LIBRARY_PATH=$PSYLLID_BUILD_PREFIX/lib:$LD_LIBRARY_PATH" >> setup.sh;
RUN /bin/true \
    && if [ -a /etc/centos-release ]; then \
        ## build setup for p8compute base image
        chmod -R 777 $PSYLLID_BUILD_PREFIX/.. \
        && echo "source ${COMMON_BUILD_PREFIX}/setup.sh" >> setup.sh \
        && echo "export PSYLLID_TAG=${PSYLLID_TAG}" >> setup.sh \
        && echo "ln -sfT $PSYLLID_BUILD_PREFIX $PSYLLID_BUILD_PREFIX/../current" >> setup.sh \
        && /bin/true;\
    elif [ -a /etc/debian_version ]; then \
        ## build setup for debian base image
        apt-get update \
        && apt-get clean \
        && apt-get --fix-missing -y install \
            build-essential \
            cmake \
            libfftw3-3 \
            libfftw3-dev \
            gdb \
            libboost-all-dev \
            libhdf5-dev \
            librabbitmq-dev \
            wget \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && /bin/true;\
    fi

WORKDIR /

########################
FROM psyllid_common as psyllid_done

COPY dripline-cpp /tmp_source/dripline-cpp
COPY external /tmp_source/external
COPY midge /tmp_source/midge
COPY monarch /tmp_source/monarch
COPY source /tmp_source/source
COPY CMakeLists.txt /tmp_source/CMakeLists.txt
COPY .git /tmp_source/.git

## store cmake args because we'll need to run twice (known package_builder issue)
## use EXTRA_CMAKE_ARGS to add or replace options at build time, CMAKE_CONFIG_ARGS_LIST are defaults
ARG EXTRA_CMAKE_ARGS=""
ENV CMAKE_CONFIG_ARGS_LIST="\
      -D CMAKE_INSTALL_PREFIX:PATH=$PSYLLID_BUILD_PREFIX \
      -D Psyllid_ENABLE_FPA=FALSE \
      ${EXTRA_CMAKE_ARGS} \
      "

RUN source $PSYLLID_BUILD_PREFIX/setup.sh \
    && mkdir -p /tmp_source/build \
    && cd /tmp_source/build \
    && cmake ${CMAKE_CONFIG_ARGS_LIST} .. \
    && cmake ${CMAKE_CONFIG_ARGS_LIST} .. \
    && make install \
    && /bin/true

########################
FROM psyllid_common

# for now we must grab the extra dependency content as well as psyllid itself
COPY --from=psyllid_done $PSYLLID_BUILD_PREFIX $PSYLLID_BUILD_PREFIX

# for a psyllid container, we need the environment to be configured, this is not desired for compute containers
# (in which case the job should start with a bare shell and then do the exact setup desired)
ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["bash"]
RUN ln -s $PSYLLID_BUILD_PREFIX/setup.sh /etc/profile.d/setup.sh
