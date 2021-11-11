# This file is part of RGBDS.
#
# Copyright (c) 2018-2019, Phil Smith and RGBDS contributors.
#
# SPDX-License-Identifier: MIT
FROM trzeci/emscripten-ubuntu:latest
ENV PKG_CONFIG_PATH=/emsdk_portable/.data/cache/asmjs/ports-builds/libpng:$PKG_CONFIG_PATH
RUN apt-get update && apt-get install byacc flex bison pkg-config libpng-dev autoconf -y
# TODO run emcc on "hello" script to set up libpng and zlib
WORKDIR /src
ENTRYPOINT ["/emsdk_portable/entrypoint"]
