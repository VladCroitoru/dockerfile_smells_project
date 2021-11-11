FROM alpine:3.4

# setup external informations
ENV BASE_URL http://www.tnlab.inf.uec.ac.jp/daihinmin/2016/files/
ENV PRODUCT_DIR /uecda
ENV WORK_DIR /work

ENV TNDHM_PKG tndhm_devkit_c-20140627
ENV TNDHM_REG default
ENV TNDHM_ARC ${TNDHM_PKG}.tar.gz
ENV TNDHM_URL ${BASE_URL}/${TNDHM_ARC}

ENV WISTERIA_PKG wisteria
ENV WISTERIA_REG wisteria
ENV WISTERIA_ARC ${WISTERIA_PKG}.tar.bz2
ENV WISTERIA_URL ${BASE_URL}/${WISTERIA_ARC}

ENV KOU2_PKG kou2
ENV KOU2_REG kou2
ENV KOU2_ARC ${KOU2_PKG}.tar.bz2
ENV KOU2_URL ${BASE_URL}/${KOU2_ARC}

# use strict
RUN set -xeuo pipefail \

# install build kit
    && apk add --no-cache wget g++ make \

# create working directory
    && mkdir -p $PRODUCT_DIR $WORK_DIR \
    && cd $WORK_DIR \

# build tndhm
    && wget $TNDHM_URL \
    && tar xvzf $TNDHM_ARC \
    && rm $TNDHM_ARC \

    && cd ${WORK_DIR}/${TNDHM_PKG}/client \
    && ./configure --enable-static \
    && make \

    && mkdir -p ${PRODUCT_DIR}/${TNDHM_REG} \
    && mv client ${PRODUCT_DIR}/${TNDHM_REG}/ \

    && cd $WORK_DIR \
    && rm -r ${TNDHM_PKG} \

# build wisteria
    && wget $WISTERIA_URL \
    && tar jxf $WISTERIA_ARC \
    && rm $WISTERIA_ARC \

    && cd ${WORK_DIR}/${WISTERIA_PKG} \
    && g++ -static -std=c++14 -flto -Ofast -o client \
        ohto/uecda/client.cc ohto/uecda/connection.c lib/dSFMT-src-2.2.3/dSFMT.c \
        -msse4.2 -mbmi -mbmi2 -m64 \
        -DHAVE_SSE2=1 -DDSFMT_MEXP=521 -DNDEBUG \

    && mkdir -p ${PRODUCT_DIR}/${WISTERIA_REG} \
    && mv client ${PRODUCT_DIR}/${WISTERIA_REG}/ \
    && mv ohto/uecda/params ${PRODUCT_DIR}/${WISTERIA_REG}/in \
    && mv ohto/uecda/params_out ${PRODUCT_DIR}/${WISTERIA_REG}/out \
    && mkdir ${PRODUCT_DIR}/${WISTERIA_REG}/log \
    && echo "${PRODUCT_DIR}/${WISTERIA_REG}/in/"  >> ${PRODUCT_DIR}/${WISTERIA_REG}/wisteria_config.txt \
    && echo "${PRODUCT_DIR}/${WISTERIA_REG}/out/" >> ${PRODUCT_DIR}/${WISTERIA_REG}/wisteria_config.txt \
    && echo "${PRODUCT_DIR}/${WISTERIA_REG}/log/" >> ${PRODUCT_DIR}/${WISTERIA_REG}/wisteria_config.txt \

    && cd $WORK_DIR \
    && rm -r ${WISTERIA_PKG} \

# build kou2
    && wget $KOU2_URL \
    && tar jxf $KOU2_ARC \
    && rm $KOU2_ARC \

    && cd ${WORK_DIR}/${KOU2_PKG} \
    && chmod +x configure \
    && ./configure --enable-static \
    && make \

    && mkdir -p ${PRODUCT_DIR}/${KOU2_REG} \
    && mv client ${PRODUCT_DIR}/${KOU2_REG}/ \

    && cd $WORK_DIR \
    && rm -r ${KOU2_PKG} \

# uninstall build kit
    && apk del --nocache --purge -r wget g++ make

# boot
WORKDIR $PRODUCT_DIR
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [""]
