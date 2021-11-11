# Shared Dockerfile for third party dependencies used in projects in the p4lang
# organization.
#
# Because multi-stage builds are relatively new and best practices aren't yet
# well established (as of this writing, at least), it's probably worth
# explaining the approach used in this Dockerfile. This Dockerfile creates a
# separate image for each third party dependency and then copies the binaries to
# a single output image at the end. If you add a new dependency, please:
#   (1) Create a new build image for it. (It should have its own FROM section.)
#   (2) Ensure that it installs everything that should be included in the final
#       image to `/output/usr/local`. Use DESTDIR and PYTHONUSERBASE for this.
#       Be sure to install python packages and code using
#       `pip install --user --ignore-installed`. If you absolutely *must* use
#       `python setup.py install`, take a look at the protobuf build image and
#       then reconsider.
#   (3) Use COPY to place the contents of the build image's `/output/usr/local`
#       in the final image.
#   (4) If the new dependency requires that certain apt packages be installed at
#       runtime (as opposed to at build time), create a new _DEPS variable and
#       install the new packages with all of the others; look at how the final
#       image is constructed and you'll understand the pattern.
# In general you don't have to worry about efficiency in the build images, but
# please minimize the amount of data and the number of layers that end up in the
# final image.

# Build ccache.
FROM ubuntu:16.04 as ccache
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV CCACHE_DEPS autoconf automake build-essential libmemcached-dev
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY ./ccache /ccache/
WORKDIR /ccache/
RUN apt-get update && apt-get install -y --no-install-recommends $CCACHE_DEPS
# Tell the ccache build system not to bother with things like documentation.
ENV RUN_FROM_BUILD_FARM=yes
RUN ./autogen.sh
RUN ./configure --enable-memcached
RUN make
# `make install` assumes that we *did* build the docs; make it happy.
RUN touch ccache.1
RUN make DESTDIR=/output install

# Build PTF.
FROM ubuntu:16.04 as ptf
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV PTF_DEPS build-essential libpcap-dev python python3 python-dev python3-dev \
    python-pip python3-pip python-setuptools python3-setuptools
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY ./ptf /ptf/
WORKDIR /ptf/
RUN apt-get update && apt-get install -y --no-install-recommends $PTF_DEPS
RUN pip install --user --ignore-installed wheel
RUN pip3 install --user --ignore-installed wheel
RUN pip install --user --ignore-installed -rrequirements.txt
RUN pip3 install --user --ignore-installed -rrequirements.txt
RUN pip install --user --ignore-installed pypcap
RUN pip3 install --user --ignore-installed pypcap
RUN pip install --user --ignore-installed .
RUN pip3 install --user --ignore-installed .

# Build nanomsg.
FROM ubuntu:16.04 as nanomsg
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV NANOMSG_DEPS build-essential cmake
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir /output
COPY ./nanomsg /nanomsg/
WORKDIR /nanomsg/
RUN apt-get update && apt-get install -y --no-install-recommends $NANOMSG_DEPS
RUN mkdir build
WORKDIR /nanomsg/build/
RUN cmake ..
RUN make DESTDIR=/output install

# Build nnpy.
FROM ubuntu:16.04 as nnpy
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV NNPY_DEPS build-essential libffi-dev python python3 python-dev python3-dev \
    python-pip python3-pip python-setuptools python3-setuptools
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY --from=nanomsg /output/usr/local /usr/local/
COPY ./nnpy /nnpy/
WORKDIR /nnpy/
RUN apt-get update && apt-get install -y --no-install-recommends $NNPY_DEPS
RUN pip install --user --ignore-installed wheel
RUN pip3 install --user --ignore-installed wheel
RUN pip install --user --ignore-installed cffi
RUN pip install --user --ignore-installed .
RUN pip3 install --user --ignore-installed cffi
RUN pip3 install --user --ignore-installed .

# Build Thrift.
FROM ubuntu:16.04 as thrift
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV THRIFT_DEPS automake \
                bison \
                build-essential \
                flex \
                libboost-dev \
                libboost-test-dev \
                libevent-dev \
                libssl1.0.0 \
                libssl-dev \
                libtool \
                pkg-config \
                python \
                python3 \
                python-dev \
                python3-dev \
                python-pip \
                python3-pip \
                python-setuptools \
                python3-setuptools
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY ./thrift /thrift/
WORKDIR /thrift/
RUN apt-get update && apt-get install -y --no-install-recommends $THRIFT_DEPS
RUN ./bootstrap.sh
RUN ./configure --with-cpp=yes \
                --with-python=yes \
                --with-c_glib=no \
                --with-java=no \
                --with-ruby=no \
                --with-erlang=no \
                --with-go=no \
                --with-nodejs=no \
                --enable-tests=no
RUN make
RUN make DESTDIR=/output install-strip
WORKDIR /thrift/lib/py/
RUN pip install --user --ignore-installed .
RUN pip3 install --user --ignore-installed .

# Build Protocol Buffers.
# The protobuf build system normally downloads archives of GMock and GTest from
# Github, but the CA certs included with Ubuntu 14.04 are so old that the
# download fails TLS verification. It's just as well, because including the
# correct versions directly in the repo is preferable anyway. These versions
# are old, though, so they're walled off in the `protobuf-deps` directory. Our
# own projects should use a more recent release.
FROM ubuntu:16.04 as protobuf
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV PROTOCOL_BUFFERS_DEPS autoconf \
                          automake \
                          ca-certificates \
                          g++ \
                          libffi-dev \
                          libtool \
                          make \
                          python-dev \
                          python3-dev \
                          python-setuptools \
                          python3-setuptools \
                          python-pip \
                          python3-pip
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY ./protobuf /protobuf/
COPY ./protobuf-deps/googlemock /protobuf/gmock
COPY ./protobuf-deps/googletest /protobuf/gmock/gtest
WORKDIR /protobuf/
RUN apt-get update && apt-get install -y --no-install-recommends $PROTOCOL_BUFFERS_DEPS
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make DESTDIR=/output install-strip
WORKDIR /protobuf/python/
# Protobuf is using a deprecated technique to install Python package with
# easy install. This is causing issues since 2021-04-21. (https://discuss.python.org/t/pypi-org-recently-changed/8433)
# We have to install pip and install six ourselves so we do not trigger the
# broken protobuf install process.
RUN pip install --user --ignore-installed wheel
RUN pip3 install --user --ignore-installed wheel
RUN pip install --user --ignore-installed six
RUN pip3 install --user --ignore-installed six
# This has been fixed in more recent Protobuf versions, but 3.6.1 does not add
# '--std=c++11' on Linux
RUN sed -i "s/extra_compile_args = \[\]/extra_compile_args = \['--std=c++11'\]/" setup.py
# We need to manually create this directory to work around a bug in protobuf's
# version of setup.py.
RUN mkdir -p /output/usr/local/lib/python2.7/site-packages
RUN python setup.py install --user --cpp_implementation
# We'll finish up the process of building protobuf below, but first, a bit of
# explanation.
#
# Since we can't use `pip` with protobuf's `setup.py`, the package gets
# installed via setuptools in an "egg" - a directory which acts as a python
# module, but isn't a package and thus isn't automatically part of the package
# namespace. Eggs need their contents to be added to python's `sys.path` to
# become visible. Hooks that run early during python startup normally read
# `setuptools.pth` and other `.pth` files and add all of the directories
# referenced in those files to the path; egg contents are placed in those files
# to be made available to the rest of the python installation.
#
# In multistage builds this doesn't work so well, because those `.pth` files can
# easily be overwritten by other versions from a different image, and the eggs
# we're installing here will no longer appear in `sys.path`. To work around
# that, we just copy the contents of the existing `.pth` files into a new one
# with a name we're sure won't be overwritten. Python will read this new `.pth`
# file at startup and include the eggs in the path.
#
# If you're wondering why the `grep -v` is necessary, meditate upon the fact
# that these files aren't merely metadata but also executable code, and
# setuptools, by design, uses this feature to inject code into every python
# program that runs on your system.
WORKDIR /output/usr/local/lib/python2.7/site-packages
RUN cat *.pth | grep -v "import sys" | sort -u > docker_protobuf.pth

# Build gRPC.
# The gRPC build system should detect that a version of protobuf is already
# installed and should not try to install the third-party one included as a
# submodule in the grpc repository.
FROM ubuntu:16.04 as grpc
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV GRPC_DEPS autoconf \
              automake \
              build-essential \
              cython \
              libtool \
              python-dev \
              python3-dev \
              python-pip \
              python3-pip \
              python-setuptools \
              python3-setuptools
ENV LDFLAGS="-Wl,-s"
RUN mkdir -p /output/usr/local
ENV PYTHONUSERBASE=/output/usr/local
COPY --from=protobuf /output/usr/local /usr/local/
RUN ldconfig
COPY ./grpc /grpc/
COPY ./grpc-constraints.txt /grpc/constraints.txt
WORKDIR /grpc/
RUN apt-get update && apt-get install -y --no-install-recommends $GRPC_DEPS
RUN make prefix=/output/usr/local
RUN make prefix=/output/usr/local install
# We don't use `--ignore-installed` here because otherwise we won't use the
# installed version of the protobuf python package that we copied from the
# protobuf build image.
RUN pip install --user -rrequirements.txt -cconstraints.txt
RUN pip3 install --user -rrequirements.txt -cconstraints.txt
RUN env GRPC_PYTHON_BUILD_WITH_CYTHON=1 pip install --user --ignore-installed .
RUN env GRPC_PYTHON_BUILD_WITH_CYTHON=1 pip3 install --user --ignore-installed .

# Build libyang
FROM ubuntu:16.04 as libyang
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
ENV LIBYANG_DEPS build-essential \
                 cmake \
                 libpcre3-dev
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir /output
COPY ./libyang /libyang/
RUN apt-get update && apt-get install -y --no-install-recommends $LIBYANG_DEPS
WORKDIR /libyang/
RUN mkdir build
WORKDIR /libyang/build/
RUN cmake ..
RUN make DESTDIR=/output install

# Build sysrepo
FROM ubuntu:16.04 as sysrepo
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
# protobuf-c is not installed as part of the protobuf image build above (it is a
# separate Github repository). It seems that installing it from the package
# manager rather than building it from source does not create any compatibility
# issue.
ENV SYSREPO_DEPS build-essential \
                 cmake \
                 libavl-dev \
                 libev-dev \
                 libprotobuf-c-dev \
                 protobuf-c-compiler
ENV CFLAGS="-Os"
ENV CXXFLAGS="-Os"
ENV LDFLAGS="-Wl,-s"
RUN mkdir /output
COPY --from=libyang /output/usr/local /usr/local/
RUN ldconfig
COPY ./sysrepo /sysrepo/
RUN apt-get update && apt-get install -y --no-install-recommends $SYSREPO_DEPS
WORKDIR /sysrepo/
RUN mkdir build
WORKDIR /sysrepo/build/
# CALL_TARGET_BINS_DIRECTLY=Off is needed here because of the use of DESTDIR
# Without it sysrepoctl is executed at install time and assumes YANG files are
# under /etc/sysrepo/yang
RUN cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=Off -DCALL_TARGET_BINS_DIRECTLY=Off ..
RUN make DESTDIR=/output install

# Construct the final image.
FROM ubuntu:16.04
MAINTAINER Seth Fowler <sfowler@barefootnetworks.com>
ARG DEBIAN_FRONTEND=noninteractive
ARG MAKEFLAGS=-j2
RUN CCACHE_RUNTIME_DEPS="libmemcached-dev" && \
    PTF_RUNTIME_DEPS="libpcap-dev python-minimal python3-minimal tcpdump" && \
    NNPY_RUNTIME_DEPS="python-minimal python3-minimal" && \
    THRIFT_RUNTIME_DEPS="libssl1.0.0 python-minimal" && \
    GRPC_RUNTIME_DEPS="python-minimal python-setuptools python3-minimal python3-setuptools" && \
    SYSREPO_RUNTIME_DEPS="libpcre3 libavl1 libev4 libprotobuf-c1" && \
    apt-get update && \
    apt-get install -y --no-install-recommends $CCACHE_RUNTIME_DEPS \
                                               $PTF_RUNTIME_DEPS \
                                               $NNPY_RUNTIME_DEPS \
                                               $THRIFT_RUNTIME_DEPS \
                                               $GRPC_RUNTIME_DEPS \
                                               $SYSREPO_RUNTIME_DEPS && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/*
# Configure ccache so that descendant containers won't need to.
COPY ./docker/ccache.conf /usr/local/etc/ccache.conf
# Copy files from the build containers.
COPY --from=ccache /output/usr/local /usr/local/
COPY --from=ptf /output/usr/local /usr/local/
COPY --from=nanomsg /output/usr/local /usr/local/
COPY --from=nnpy /output/usr/local /usr/local/
COPY --from=thrift /output/usr/local /usr/local/
COPY --from=protobuf /output/usr/local /usr/local/
COPY --from=grpc /output/usr/local /usr/local/
COPY --from=libyang /output/usr/local /usr/local/
COPY --from=sysrepo /output/usr/local /usr/local/
COPY --from=sysrepo /output/etc /etc/
# `pip install --user` will place things in `site-packages`, but Ubuntu expects
# `dist-packages` by default, so we need to set configure `site-packages` as an
# additional "site-specific directory".
RUN export PYTHON3_VERSION=`python3 -c 'import sys; version=sys.version_info[:3]; print("python{0}.{1}".format(*version))'` && \
  echo "import site; site.addsitedir('/usr/local/lib/$PYTHON3_VERSION/site-packages')" \
    > /usr/local/lib/$PYTHON3_VERSION/dist-packages/use_site_packages.pth
RUN export PYTHON2_VERSION=`python2 -c 'import sys; version=sys.version_info[:3]; print("python{0}.{1}".format(*version))'` && \
  echo "import site; site.addsitedir('/usr/local/lib/$PYTHON2_VERSION/site-packages')" \
    > /usr/local/lib/$PYTHON2_VERSION/dist-packages/use_site_packages.pth

RUN ldconfig
