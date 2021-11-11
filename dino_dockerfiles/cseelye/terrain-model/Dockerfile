# GDAL version to use
ARG GDAL_VERSION="3.3.2"
# Blender version to use
ARG BLENDER_BRANCH="blender-v2.93-release"
# Python version to use - this must match what blender is expecting
ARG PYTHON_VERSION="3.9.2"
# Number CPU cores to limit to while building
ARG CORES=8

#
# Primordial base stage
# Shared base layers for all other stages
#
FROM ubuntu:20.04 AS primordial

ARG CORES
ARG GDAL_VERSION
ARG BLENDER_BRANCH
ARG PYTHON_VERSION
ARG PROJ_INSTALL_PREFIX=/usr/local
ARG GDAL_DEST=/build_gdal
ARG GCC_ARCH=x86_64

# Configure apt to never install recommended packages and do not prompt for user input
RUN printf 'APT::Install-Recommends "0";\nAPT::Install-Suggests "0";\n' >> /etc/apt/apt.conf.d/01norecommends
ENV DEBIAN_FRONTEND=noninteractive

# Set locale and timezone
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && \
    apt-get install --yes locales tzdata && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    locale-gen "en_US.UTF-8"
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Install common packages and python dependencies
RUN apt-get update && \
    apt-get install --yes \
        ca-certificates \
        curl \
        gnupg \
        libreadline8 \
        libncursesw6 \
        libssl1.1 \
        libsqlite3-0 \
        libtk8.6 \
        libgdbm6 \
        libbz2-1.0 \
        libffi7 \
    && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/*

#
# Python build stage
#
# Here we build python from source instead of installing from a repo because
# as of this writing, python on debian-based distros do not include distutils,
# which is required to use pip and install modules. Installing 
# python3.9-distutils also installs python 3.8 as a dependency (because that is
# the "system" python3 in ubuntu 20.04). Instead, if we install completely from
# source we can get a full working python3.9 including distutils without
# dragging in python3.8. All of this stems from the fact that debian splits up
# python and repackages it as separate runtime and development pieces.
FROM primordial AS build_python
RUN apt-get update && \
    apt-get install --yes \
        build-essential \
        checkinstall \
        libreadline-gplv2-dev \
        libncursesw5-dev \
        libssl-dev \
        libsqlite3-dev \
        tk-dev \
        libgdbm-dev \
        libc6-dev \
        libbz2-dev \
        libffi-dev
RUN curl -LSsf https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz | tar -xz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations --prefix=/build_python3.9 && \
    make -j${CORES} && \
    make install

#
# Base stage
# Shared layers all other stages share (primordial layers plus python runtime)
#
FROM primordial AS base
COPY --from=build_python /build_python3.9 /usr/
RUN ldconfig


#
# GDAL build stage
#
FROM base AS build_gdal

# Install build tools
RUN apt-get update && \
    apt-get install --yes \
        autoconf \
        automake \
        bash \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        git \
        gnupg \
        libtool \
        make \
        pkg-config \
        unzip

# PROJ dependencies
RUN apt-get install --yes \
        libcurl4-gnutls-dev \
        libsqlite3-dev \
        libtiff5-dev \
        sqlite3 \
        zlib1g-dev

# GDAL dependencies
RUN apt-get install --yes \
        libexpat-dev \
        libgeos-dev \
        libjpeg-dev \
        libopenjp2-7-dev \
        libpng-dev \
        libpq-dev \
        libssl-dev \
        libwebp-dev \
        libxerces-c-dev \
        libzstd-dev \
        sqlite3

# Get the source and build PROJ and GDAL
COPY container_build/build-proj container_build/build-gdal /
RUN /build-proj
RUN /build-gdal


#
# Blender build stage
#
FROM base AS build_blender

# Install build tools and other required tools/libraries
RUN apt-get update && \
    apt-get install --yes \
        build-essential \
        cmake \
        git \
        libx11-dev \
        libxxf86vm-dev \
        libxcursor-dev \
        libxi-dev \
        libxrandr-dev \
        libxinerama-dev \
        libglew-dev \
        subversion \
        sudo \
        wget \
    && \
    git config --global user.email "buildscript@blender-build.invalid" && git config --global user.name "Build Script" && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/*

# To speed up debugging/iteration on the container image, checkout the blender
# source in your build context and uncomment the COPY line to copy it into the
# container instead of checking it out every time.
#   mkdir -p container_build/blender-build/lib
#   git clone --depth 1 --branch blender-v2.93-release --single-branch https://git.blender.org/blender.git container_build/blender-build/blender-src
#   svn --non-interactive checkout https://svn.blender.org/svnroot/bf-blender/tags/blender-2.93-release/lib/linux_centos7_x86_64 container_build/blender-build/lib/linux_centos7_x86_64
#COPY container_build/ /

# Get the blender source and build/install the bpy python module.
# This creates a "user" install which is easy to copy from /root/.local
COPY container_build/build-bpy /
RUN /build-bpy

#
# Python modules build stage
#
FROM base AS build_py_modules

# Install other python modules into python
# This creates a "user" install which is easy to copy from /root/.local
COPY requirements.txt /tmp/
RUN curl https://bootstrap.pypa.io/get-pip.py | python3 && \
    python3 -m pip --no-cache-dir install --upgrade --requirement=/tmp/requirements.txt --user && \
    rm --force /tmp/requirements.txt

#
# Production image stage
#
FROM base AS prod

# Install runtime dependencies for PROJ and GDAL
RUN apt-get update && \
    apt-get install --yes \
        libcurl4 \
        libexpat1 \
        libgeos-3.8.0 \
        libgeos-c1v5 \
        libjpeg-turbo8 \
        libopenjp2-7 \
        libpng16-16 \
        libpq5 \
        libsqlite3-0 \
        libssl1.1 \
        libtiff5 \
        libwebp6 \
        libxerces-c3.2 \
        libzstd1 \
    && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install runtime dependencies for blender
RUN apt-get update && \
    apt-get install --yes \
        libx11-6 \
        libxxf86vm1 \
        libxfixes3 \
        libxrender1 \
        libgl1 \
        libgomp1 \
        openscad \
    && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the PROJ/GDAL modules from the gdal build stage
COPY --from=build_gdal ${GDAL_DEST} /

# Copy the python modules from the blender build stage
COPY --from=build_blender /root/.local /usr/lib/python3.9/

# Copy the python modules from the python module build stage
COPY --from=build_py_modules /root/.local /usr/

# Run ldconfig to make sure shared libraries are configured correctly
RUN ldconfig


#
# Dev image stage - adds tools useful for development but not necessary for
# runtime
#
FROM prod AS dev
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install --yes \
        git \
        tree \
        vim \
        && \
    apt-get autoremove --yes && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    curl https://bootstrap.pypa.io/get-pip.py | python3
COPY requirements*.txt /tmp/
RUN python3 -m pip install --no-cache-dir --upgrade --user --requirement /tmp/requirements-dev.txt && \
    python3.9 -m pip install --no-cache-dir --upgrade --user --requirement /tmp/requirements-dev.txt && \
    rm --force /tmp/requirements*.txt
