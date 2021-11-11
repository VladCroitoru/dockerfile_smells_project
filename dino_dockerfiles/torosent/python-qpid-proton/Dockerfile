ARG PYTHON_IMAGE_VERSION=3.6-slim-stretch

FROM python:${PYTHON_IMAGE_VERSION} AS build

ARG PROTON_VERSION=0.18.1

# Required dependencies
RUN apt-get update && apt-get install -y git gcc cmake cmake-curses-gui uuid-dev libssl-dev libsasl2-2 \
    libsasl2-dev swig python-epydoc

# Build qpid proton
RUN git clone https://github.com/apache/qpid-proton.git && \
    cd qpid-proton && git checkout tags/${PROTON_VERSION} && mkdir build && cd build && \
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_PHP=OFF -DBUILD_PERL=OFF -DBUILD_RUBY=OFF -DSYSINSTALL_BINDINGS=ON && \
    make install && \
    rm -rf /qpid-proton

# Proton runtime
FROM python:${PYTHON_IMAGE_VERSION}

ARG PYTHON_DIR_VERSION=3.6

RUN apt-get update && apt-get install -y git libsasl2-2 swig && \
    rm -rf /var/lib/apt/lists/*

# Proton runtime and dependencies
COPY --from=build /usr/include/proton/ /usr/include/proton/
COPY --from=build /usr/lib/libqpid* /usr/lib/
COPY --from=build /usr/local/lib/python${PYTHON_DIR_VERSION}/ /usr/local/lib/python${PYTHON_DIR_VERSION}/
COPY --from=build /usr/lib/cmake/Proton/ /usr/lib/cmake/Proton/
COPY --from=build /usr/lib/pkgconfig/libqpid* /usr/lib/pkgconfig/
