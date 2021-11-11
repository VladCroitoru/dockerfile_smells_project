FROM project8/p8compute_dependencies:v1.0.0 as morpho_common

ENV MORPHO_TAG=v2.7.2
ENV MORPHO_BUILD_PREFIX=/usr/local/p8/morpho/$MORPHO_TAG

RUN mkdir -p $MORPHO_BUILD_PREFIX &&\
    chmod -R 777 $MORPHO_BUILD_PREFIX/.. &&\
    cd $MORPHO_BUILD_PREFIX &&\
    echo "source ${COMMON_BUILD_PREFIX}/setup.sh" > setup.sh &&\
    echo "export MORPHO_TAG=${MORPHO_TAG}" >> setup.sh &&\
    echo "export MORPHO_BUILD_PREFIX=${MORPHO_BUILD_PREFIX}" >> setup.sh &&\
    echo 'ln -sfT $MORPHO_BUILD_PREFIX $MORPHO_BUILD_PREFIX/../current' >> setup.sh &&\
    echo 'export PATH=$MORPHO_BUILD_PREFIX/bin:$PATH' >> setup.sh &&\
    echo 'export LD_LIBRARY_PATH=$MORPHO_BUILD_PREFIX/lib:$LD_LIBRARY_PATH' >> setup.sh &&\
    echo 'export PYTHONPATH=$MORPHO_BUILD_PREFIX/$(python3 -m site --user-site | sed "s%$(python3 -m site --user-base)%%"):$PYTHONPATH' >> setup.sh &&\
    /bin/true

########################
FROM morpho_common as morpho_done

COPY bin /tmp_source/bin
COPY examples /tmp_source/examples
COPY morpho /tmp_source/morpho
COPY setup.py /tmp_source/setup.py
COPY .git /tmp_source/.git

COPY tests $MORPHO_BUILD_PREFIX/tests

RUN source $MORPHO_BUILD_PREFIX/setup.sh &&\
    cd /tmp_source &&\
    pip3 install setuptools-scm &&\
    pip3 install . --prefix $MORPHO_BUILD_PREFIX &&\
    /bin/true

########################
FROM morpho_common

COPY --from=morpho_done $MORPHO_BUILD_PREFIX $MORPHO_BUILD_PREFIX
