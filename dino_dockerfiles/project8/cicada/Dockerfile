FROM project8/p8compute_dependencies:v0.3.0 as cicada_common

ARG build_type=Release
ENV CICADA_BUILD_TYPE=$build_type

ENV CICADA_TAG=v1.3.2
ENV CICADA_BUILD_PREFIX=/usr/local/p8/cicada/$CICADA_TAG

RUN mkdir -p $CICADA_BUILD_PREFIX &&\
    cd $CICADA_BUILD_PREFIX &&\
    echo "source ${COMMON_BUILD_PREFIX}/setup.sh" > setup.sh &&\
    echo "export CICADA_TAG=${CICADA_TAG}" >> setup.sh &&\
    echo "export CICADA_BUILD_PREFIX=${CICADA_BUILD_PREFIX}" >> setup.sh &&\
    echo 'ln -sf $CICADA_BUILD_PREFIX $CICADA_BUILD_PREFIX/../current || /bin/true' >> setup.sh &&\
    echo 'export PATH=$CICADA_BUILD_PREFIX/bin:$PATH' >> setup.sh &&\
    echo 'export LD_LIBRARY_PATH=$CICADA_BUILD_PREFIX/lib:$LD_LIBRARY_PATH' >> setup.sh &&\
    /bin/true

########################
FROM cicada_common as cicada_done

COPY Library /tmp_source/Library
COPY Scarab /tmp_source/Scarab
COPY CMakeLists.txt /tmp_source/CMakeLists.txt
COPY this_cicada.sh.in /tmp_source/this_cicada.sh.in
COPY .git /tmp_source/.git

# repeat the cmake command to get the change of install prefix to set correctly (a package_builder known issue)
RUN source $CICADA_BUILD_PREFIX/setup.sh &&\
    cd /tmp_source &&\
    mkdir build &&\
    cd build &&\
    cmake -D CMAKE_BUILD_TYPE=$CICADA_BUILD_TYPE \
          -D CMAKE_INSTALL_PREFIX:PATH=$CICADA_BUILD_PREFIX \
          -D CMAKE_SKIP_INSTALL_RPATH:BOOL=True .. &&\
    cmake -D CMAKE_BUILD_TYPE=$CICADA_BUILD_TYPE \
          -D CMAKE_INSTALL_PREFIX:PATH=$CICADA_BUILD_PREFIX \
          -D CMAKE_SKIP_INSTALL_RPATH:BOOL=True .. &&\
    make -j3 install &&\
    /bin/true

########################
FROM cicada_common

COPY --from=cicada_done $CICADA_BUILD_PREFIX $CICADA_BUILD_PREFIX
