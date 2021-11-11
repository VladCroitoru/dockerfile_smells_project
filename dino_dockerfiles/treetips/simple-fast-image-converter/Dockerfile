FROM python:alpine3.6
LABEL  maintainer "tree <treetips555@gmail.com>"

RUN apk update && \
    apk --update add \
        libxml2-dev \
        libxslt-dev \
        libffi-dev \
        gcc \
        musl-dev \
        libgcc \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev && \
    # https://github.com/uploadcare/pillow-simd#installation
    CC="cc -mavx2" pip install -U --force-reinstall pillow-simd
