# python 373 with oraclelinux:7
ARG PYPI_BUILD_DEPS="gcc gcc-c++"
ARG PYPI_DEPS=""
ARG PYTHON_VERSION=3.7.3
ARG PYTHON_PIP_VERSION=20.1.1
ARG ORA_VERSION=19.5

FROM oraclelinux:7-slim AS base
ARG SYSTEM_DEPS="bzip2 gnupg2 gzip tar tzdata which xz"
ARG PYTHON_DEPS="bzip2-libs expat gdbm glibc keyutils-libs krb5-libs libcom_err libffi libselinux \
                 libuuid ncurses-libs nss-softokn-freebl openssl-libs pcre readline sqlite \
                 xz-libs zlib"
ARG SQLITE_DEPS="tcl"

# Update the system and install runtime dependencies
RUN : \
 && set -ex \
 && yum clean all \
 && /usr/bin/ol_yum_configure.sh \
 && yum -y upgrade \
 && yum -y install $SYSTEM_DEPS $PYTHON_DEPS $SQLITE_DEPS \
 && yum clean all \
 && rm -rf /var/cache/yum/ /var/lib/yum/repos/*
# base }}}

FROM base AS oracle-base

ARG ORA_VERSION

ENV PATH=${_bin}:$PATH:/usr/lib/oracle/${ORA_VERSION}/client64/bin

RUN : \
 && set -ex \
 && yum clean all \
 && curl -sSLo /etc/yum.repos.d/public-yum-ol7.repo https://yum.oracle.com/public-yum-ol7.repo \
 && yum-config-manager --enable ol7_oracle_instantclient \
 && yum -y install oracle-instantclient${ORA_VERSION}-basic oracle-instantclient${ORA_VERSION}-sqlplus \
 && echo /usr/lib/oracle/${ORA_VERSION}/client64/lib >/etc/ld.so.conf.d/oracle-instantclient${ORA_VERSION}.conf \
 && ldconfig \
 && yum clean all \
 && rm -rf /var/cache/yum/ /var/lib/yum/repos/*
# }}}

FROM base AS builder

ARG PYTHON_PIP_VERSION
ARG PYTHON_VERSION
ARG pybasever=3.7
ARG pyshortver=37
ARG _bindir=/usr/local/bin
ARG _libdir=/usr/local/lib
ARG pylibdir=${_libdir}/python${pybasever}
ARG dynload_dir=${pylibdir}/lib-dynload
ARG ABIFLAGS_optimized=m
ARG _arch=x86_64
ARG _gnu=-gnu
ARG bytecode_suffixes=.cpython-${pyshortver}*.pyc
ARG SOABI_optimized=cpython-${pyshortver}${ABIFLAGS_optimized}-${_arch}-linux${_gnu}
ARG PYTHON_BUILD_DEPS="gcc gcc-c++ bzip2-devel glibc-devel expat-devel libffi-devel gdbm-devel \
                       xz-devel ncurses-devel readline-devel sqlite-devel openssl-devel make \
                       tk-devel libuuid-devel zlib-devel"
ARG SQLITE_BUILD_DEPS="autoconf file pkgconfig ncurses-devel readline-devel glibc-devel tcl-devel"
ARG SQLITE_VERSION=3320300

ENV PATH=$_bindir:$PATH

WORKDIR /usr/src

# Install build dependencies
RUN : \
 && set -ex \
 && yum clean all \
 && yum -y install $PYTHON_BUILD_DEPS $SQLITE_BUILD_DEPS

# Install SQLite
RUN : \
 && set -ex \
 && curl -sSLo sqlite.tar.gz "https://sqlite.org/2020/sqlite-autoconf-${SQLITE_VERSION}.tar.gz" \
 && mkdir -p /usr/src/sqlite \
 && tar -xzC /usr/src/sqlite --strip-components=1 -f sqlite.tar.gz \
 && rm sqlite.tar.gz

# Build and install SQLite
RUN : \
 && set -ex \
 && cd /usr/src/sqlite \
 && sh ./configure \
         --disable-static \
         --enable-silent-rules \
 && make -j $(nproc) \
 && make install

# Extract python source
RUN : \
 && set -ex \
 && curl -sSLo python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
 && mkdir -p /usr/src/python \
 && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
 && rm python.tar.xz

# Build and install python. Run ldconfig to get the libraries in LD_LIBRARY_PATH
# NOTE: Don't forget to `ldconfig` in the COPY destination later.
RUN : \
 && set -ex \
 && cd /usr/src/python \
 && CXX="/usr/bin/g++" sh ./configure \
         --enable-ipv6 \
         --enable-shared \
         --with-dbmliborder=gdbm:ndbm:bdb \
         --with-system-expat \
         --enable-loadable-sqlite-extensions \
         --without-ensurepip \
         --with-lto \
 && make -j "$(nproc)" \
 && make install

# Make sure python3 runs. If anything fails silently, this should catch it by throwing a runtime error
# NOTE: This ldconfig is only for this stage - it doesn't carryover.
RUN : \
 && set -ex \
 && echo ${_libdir} >/etc/ld.so.conf.d/usr-local-py3.conf \
 && ldconfig \
 && python3 --version

# make some useful symlinks that are expected to exist
RUN : \
 && set -ex \
 && cd ${_bindir} \
 && ln -s pydoc3 pydoc \
 && ln -s python3 python \
 && ln -s python3-config python-config

# Get and install pip
# Make sure pip runs. If anything fails silently, this should catch it by throwing a runtime error
RUN : \
 && set -ex \
 && curl -sSLo get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \
 && python get-pip.py \
      --disable-pip-version-check \
      --no-cache-dir \
      "pip==$PYTHON_PIP_VERSION" \
 && pip --version \
 && rm -f get-pip.py

# Cleanup files that we don't want to have in the final image
RUN : \
 && set -ex \
# %files libs
 && rm -rf \
      ${pylibdir}/distutils/command/wininst-*.exe \
      ${pylibdir}/turtle.py \
      ${pylibdir}/__pycache__/turtle*${bytecode_suffixes} \
# %files idle
      ${_bindir}/idle* \
      ${pylibdir}/idlelib \
# %files tkinter
      ${pylibdir}/tkinter \
      ${dynload_dir}/_tkinter.${SOABI_optimized}.so \
      ${pylibdir}/turtledemo \
# Python bytecode
 && find ${pylibdir} -type d -name __pycache__ -exec rm -rf '{}' +
# }}}


FROM oracle-base AS python-oracle
COPY --from=builder /etc/ld.so.conf.d/usr-local-py3.conf /etc/ld.so.conf.d/usr-local-py3.conf
COPY --from=builder /usr/local/ /usr/local/
RUN ldconfig

MAINTAINER Mastercard udap team
WORKDIR /opt/work
ARG ANALYTICS_ZOO_VERSION=0.10.0-SNAPSHOT
ARG BIGDL_VERSION=0.12.1
ARG SPARK_VERSION=3.0.0
ARG RUNTIME_SPARK_MASTER=local[*]
ARG RUNTIME_DRIVER_CORES=1
ARG RUNTIME_DRIVER_MEMORY=2g
ARG RUNTIME_EXECUTOR_CORES=2
ARG RUNTIME_EXECUTOR_MEMORY=8g
ARG RUNTIME_TOTAL_EXECUTOR_CORES=2
ENV ANALYTICS_ZOO_VERSION           ${ANALYTICS_ZOO_VERSION}
ENV SPARK_VERSION                   ${SPARK_VERSION}
ENV BIGDL_VERSION                   ${BIGDL_VERSION}
ENV RUNTIME_SPARK_MASTER            ${RUNTIME_SPARK_MASTER}
ENV RUNTIME_DRIVER_CORES            ${RUNTIME_DRIVER_CORES}
ENV RUNTIME_DRIVER_MEMORY           ${RUNTIME_DRIVER_MEMORY}
ENV RUNTIME_EXECUTOR_CORES          ${RUNTIME_EXECUTOR_CORES}
ENV RUNTIME_EXECUTOR_MEMORY         ${RUNTIME_EXECUTOR_MEMORY}
ENV RUNTIME_TOTAL_EXECUTOR_CORES    ${RUNTIME_TOTAL_EXECUTOR_CORES}
ENV SPARK_HOME                      /opt/work/spark-${SPARK_VERSION}
ENV ANALYTICS_ZOO_HOME              /opt/work/analytics-zoo-${ANALYTICS_ZOO_VERSION}
ENV PYTHONPATH 		                ${ANALYTICS_ZOO_HOME}/lib/analytics-zoo-bigdl_${BIGDL_VERSION}-spark_${SPARK_VERSION}-${ANALYTICS_ZOO_VERSION}-python-api.zip
ENV JAVA_HOME                       /opt/jdk
ENV PATH                            ${JAVA_HOME}/bin:${PATH}

RUN yum -y install \
    ca-certificates \
    cronie \
    curl \
    gnupg2 \
    initscripts \
    iptables \
    iputils \
    lsof \
    nc \
    net-tools \
    nmap \
    openssl \
    passwd \
    procps \
    strace \
    sudo \
    systemd-sysv \
    system-lsb-core \
    tcpdump \
    telnet \
    util-linux \
    vim-minimal \
    vim \
    git \
    nano \
    zip \
    unzip \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    which \
    automake \
    autoconf \
    libtool \
    make \
    gcc \
    gcc-c++ \
    numactl \
    yum clean all && \
    rm -rf /var/cache/yum && \
    rm -rf /var/log/*

CMD [ "/usr/lib/systemd/systemd" ]

#java
RUN wget http://enos.itcollege.ee/~jpoial/allalaadimised/jdk8/jdk-8u291-linux-x64.tar.gz && \
    gunzip jdk-8u291-linux-x64.tar.gz && \
    tar -xf jdk-8u291-linux-x64.tar -C /opt && \
    rm jdk-8u291-linux-x64.tar && \
    ln -s /opt/jdk1.8.0_291 /opt/jdk

ARG MAVEN_VERSION=3.5.4
# Maven
RUN curl -fsSL https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_VERSION=${MAVEN_VERSION}
ENV M2_HOME /usr/share/maven
ENV maven.home $M2_HOME
ENV M2 $M2_HOME/bin
ENV PATH $M2:$PATH


#python libs
COPY conf/requirements.txt requirements.txt
RUN pip install --upgrade setuptools wheel && \
    pip install -r requirements.txt && \
    pip install spylon-kernel && \
    python -m spylon_kernel install


#spark
ENV SPARK_CONF_DIR=$SPARK_HOME/conf
ENV PATH $PATH:$SPARK_HOME/bin
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz && \
    tar -zxvf spark-${SPARK_VERSION}-bin-hadoop3.2.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop3.2 spark-${SPARK_VERSION} && \
    rm spark-${SPARK_VERSION}-bin-hadoop3.2.tgz

ADD conf/spark-env.sh ${SPARK_HOME}/conf/
ADD conf/spark-defaults.conf ${SPARK_HOME}/conf/

# Adding data files
RUN mkdir -p /opt/work/data
ADD data/*.* /opt/work/data/
RUN chmod a+x /opt/work/data/*.*


# Adding scripts files 
RUN mkdir -p /opt/work/scripts
ADD scripts/*.* /opt/work/scripts/
RUN chmod a+x /opt/work/scripts/*.*

# Adding ncf 
RUN mkdir -p /opt/work/examples
RUN mkdir -p /opt/work/examples/ncf
ADD ncf/*.* /opt/work/examples/ncf/
RUN chmod a+x /opt/work/examples/ncf/*.*
RUN mkdir -p /opt/work/model
RUN mkdir -p /opt/work/model/ncf
RUN mkdir -p /opt/work/logs
RUN mkdir -p /opt/work/logs/ncf
RUN mkdir -p /opt/work/output
RUN mkdir -p /opt/work/output/ncf
RUN mkdir -p /opt/work/metrics
RUN mkdir -p /opt/work/metrics/ncf
	
# Download zoo 
RUN /opt/work/scripts/download-analytics-zoo.sh


EXPOSE 22
EXPOSE 4040
EXPOSE 6006
EXPOSE 8080
EXPOSE 8998
EXPOSE 10000
EXPOSE 12345

CMD ["bash"]

