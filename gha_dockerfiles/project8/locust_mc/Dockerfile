FROM project8/p8compute_dependencies:v0.9.0 as locust_common

ARG build_type=Release
ENV LOCUST_BUILD_TYPE=$build_type

ENV LOCUST_TAG=v2.2.0
ENV LOCUST_BUILD_PREFIX=/usr/local/p8/locust/$LOCUST_TAG

RUN mkdir -p $LOCUST_BUILD_PREFIX &&\
    chmod -R 777 $LOCUST_BUILD_PREFIX/.. &&\
    cd $LOCUST_BUILD_PREFIX &&\
    echo "source ${COMMON_BUILD_PREFIX}/setup.sh" > setup.sh &&\
    echo "export LOCUST_TAG=${LOCUST_TAG}" >> setup.sh &&\
    echo "export LOCUST_BUILD_PREFIX=${LOCUST_BUILD_PREFIX}" >> setup.sh &&\
    echo 'ln -sfT $LOCUST_BUILD_PREFIX $LOCUST_BUILD_PREFIX/../current' >> setup.sh &&\
    echo 'export PATH=$LOCUST_BUILD_PREFIX/bin:$PATH' >> setup.sh &&\
    echo 'export LD_LIBRARY_PATH=$LOCUST_BUILD_PREFIX/lib:$LD_LIBRARY_PATH' >> setup.sh &&\
    echo 'export LD_LIBRARY_PATH=$LOCUST_BUILD_PREFIX/lib64:$LD_LIBRARY_PATH' >> setup.sh &&\
    /bin/true

########################
FROM locust_common as locust_done

COPY Config /tmp_source/Config
COPY Data /tmp_source/Data
COPY kassiopeia /tmp_source/kassiopeia
COPY monarch /tmp_source/monarch
COPY Scarab /tmp_source/Scarab
COPY Source /tmp_source/Source
COPY Config /tmp_source/Config
COPY CMakeLists.txt /tmp_source/CMakeLists.txt
COPY .git /tmp_source/.git

# repeat the cmake command to get the change of install prefix to set correctly (a package_builder known issue)
RUN source $LOCUST_BUILD_PREFIX/setup.sh &&\
    cd /tmp_source &&\
    mkdir build &&\
    cd build &&\
    cmake -D CMAKE_BUILD_TYPE=$LOCUST_BUILD_TYPE \
          -D CMAKE_INSTALL_PREFIX:PATH=$LOCUST_BUILD_PREFIX \
          -D DATA_INSTALL_DIR=$LOCUST_BUILD_PREFIX/data \
          -D locust_mc_BUILD_WITH_KASSIOPEIA=TRUE .. &&\
    cmake -D CMAKE_BUILD_TYPE=$LOCUST_BUILD_TYPE \
          -D CMAKE_INSTALL_PREFIX:PATH=$LOCUST_BUILD_PREFIX \
          -D DATA_INSTALL_DIR=$LOCUST_BUILD_PREFIX/data \
          -D locust_mc_BUILD_WITH_KASSIOPEIA=TRUE .. &&\
    make -j3 install &&\
    /bin/true


########################
FROM locust_common

COPY --from=locust_done $LOCUST_BUILD_PREFIX $LOCUST_BUILD_PREFIX
