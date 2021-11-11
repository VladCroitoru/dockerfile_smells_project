FROM python:3.5-alpine

ENV NUMPY_VERSION="1.11.2" \
    OPENBLAS_VERSION="0.2.18"

RUN echo "http://alpine.gliderlabs.com/alpine/v3.4/main" > /etc/apk/repositories \
    && echo "http://alpine.gliderlabs.com/alpine/v3.4/community" >> /etc/apk/repositories \
    && echo "@edge http://alpine.gliderlabs.com/alpine/edge/community" >> /etc/apk/repositories \
    && apk --no-cache add openblas-dev@edge

RUN export NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
    && apk --no-cache add --virtual build-deps \
        musl-dev \
        linux-headers \
        g++ \
    && cd /tmp \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install cython \
    && cd /tmp \
    && wget http://downloads.sourceforge.net/project/numpy/NumPy/$NUMPY_VERSION/numpy-$NUMPY_VERSION.tar.gz \
    && tar -xzf numpy-$NUMPY_VERSION.tar.gz \
    && rm numpy-$NUMPY_VERSION.tar.gz \
    && cd numpy-$NUMPY_VERSION/ \
    && cp site.cfg.example site.cfg \
    && echo -en "\n[openblas]\nlibraries = openblas\nlibrary_dirs = /usr/lib\ninclude_dirs = /usr/include\n" >> site.cfg \
    && python -q setup.py build -j ${NPROC} --fcompiler=gfortran install \
    && cd /tmp \
    && rm -r numpy-$NUMPY_VERSION \
    && pip install numexpr pandas scipy \
    && apk --no-cache del --purge build-deps
